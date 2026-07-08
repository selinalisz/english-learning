import argparse
import asyncio
import json
import re
import ssl
from datetime import datetime, timedelta
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


def list_date_folders(daily_dir: Path) -> list[str]:
    dates = []
    for child in daily_dir.iterdir():
        if not child.is_dir():
            continue
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", child.name):
            continue
        if (child / "index.html").exists():
            dates.append(child.name)
    dates.sort(reverse=True)
    return dates


def find_due_review_words(learning_words: list[dict], today: str, count: int = 3) -> list[dict]:
    due = []
    for w in learning_words:
        if int(w.get("reviewCount", 0)) >= 7:
            continue
        if w.get("nextReview", "9999-99-99") <= today:
            due.append(w)
    due.sort(key=lambda x: (x.get("nextReview", "9999-99-99"), x.get("word", "")))
    return due[:count]


def has_pos_tag(entry: dict, tags: set[str]) -> bool:
    pos_text = entry.get("partOfSpeech", "").lower()
    tokens = set(re.findall(r"[a-z]+", pos_text))
    return not tags.isdisjoint(tokens)


def pick_story_review_slots(due_words: list[dict]) -> tuple[str, str, str]:
    noun_candidates = [w for w in due_words if has_pos_tag(w, {"n", "noun"})]
    rw1 = noun_candidates[0]["word"] if noun_candidates else "history"

    noun2_pool = [w for w in noun_candidates if w["word"] != rw1]
    rw2 = noun2_pool[0]["word"] if noun2_pool else "reason"

    noun3_pool = [w for w in noun2_pool if w["word"] != rw2]
    rw3 = noun3_pool[0]["word"] if noun3_pool else "result"

    return rw1, rw2, rw3


def choose_new_words(ket_words: list[dict], learning_words: list[dict]) -> list[dict]:
    learned = {w.get("word", "").lower() for w in learning_words}
    candidates = [
        w for w in ket_words
        if w.get("word")
        and w["word"].lower() not in learned
        and " " not in w["word"]
    ]
    if len(candidates) < 3:
        raise ValueError("Not enough unseen KET words to generate today's draft")

    def has_pos(entry: dict, token: str) -> bool:
        return token in entry.get("partOfSpeech", "").lower()

    preferred_adj = ["latest", "correct", "possible", "general", "public", "local"]
    preferred_nouns = ["reason", "answer", "fact", "difference", "idea", "address"]

    by_word = {w["word"].lower(): w for w in candidates}

    w1 = next((by_word[x] for x in preferred_adj if x in by_word and has_pos(by_word[x], "adj")), None)
    if not w1:
        w1 = next((w for w in candidates if has_pos(w, "adj")), candidates[0])

    pool_n = [w for w in candidates if w["word"].lower() != w1["word"].lower() and has_pos(w, "n")]
    by_word_n = {w["word"].lower(): w for w in pool_n}

    w2 = next((by_word_n[x] for x in preferred_nouns if x in by_word_n), None)
    if not w2:
        w2 = pool_n[0] if pool_n else next(w for w in candidates if w["word"].lower() != w1["word"].lower())

    pool_n2 = [w for w in pool_n if w["word"].lower() != w2["word"].lower()]
    by_word_n2 = {w["word"].lower(): w for w in pool_n2}
    w3 = next((by_word_n2[x] for x in preferred_nouns if x in by_word_n2), None)
    if not w3:
        w3 = pool_n2[0] if pool_n2 else next(
            w for w in candidates if w["word"].lower() not in {w1["word"].lower(), w2["word"].lower()}
        )

    return [w1, w2, w3]


def pick_story_variant(episode_num: int) -> dict:
    variants = [
        {
            "story": "The Blue Receipt",
            "sentences": [
                "At 8:09, Mina stood between two buses at the gate.",
                "The blue screen showed Route 8:10 to River Street.",
                "The gray screen showed Route 8:10 to Old Tunnel.",
                "Mina checked route {rw1} on the old phone.",
                "Mina saw the word {w1} on a notice in one second.",
                "Mina asked a worker for help near the gate.",
                "She asked which bus stops at River Street.",
                "The worker said to check the printed board first.",
                "The printed board did not show the blue bus line.",
                "Mina wrote the word {w2} in her notebook.",
                "Lina texted that someone was editing the station system.",
                "Mina asked for the {rw2} behind this trick.",
                "Lina replied seat 12 is only on the blue bus.",
                "Mina used the map to compare stop names.",
                "One stop did not match her old {rw3}.",
                "Mina decided to get on the gray bus.",
                "The blue bus left first and turned at the corner.",
                "The old phone showed a message: You are on the safe side.",
            ],
            "phrases": [
                ("get on", "Phrasal Verb", "上车", "文章用法：Mina decided to get on the gray bus."),
                ("ask for help", "Phrasal Verb", "寻求帮助", "文章用法：Mina asked a worker for help near the gate."),
                ("route history", "Collocation", "路线记录", "文章用法：Mina checked route history on the old phone."),
                ("printed board", "Collocation", "纸质告示牌", "文章用法：The worker said to check the printed board first."),
                ("in one second", "Fixed Expression", "在一秒内", "文章用法：The notice changed in one second."),
                ("safe side", "Fixed Expression", "安全的一侧", "文章用法：You are on the safe side."),
            ],
            "quiz": {
                "q1": "1. Which source did the worker tell Mina to trust?",
                "q1_opts": [("A", "The app screen", False), ("B", "The printed board", True), ("C", "A random post", False), ("D", "The cafe menu", False)],
                "q3": "3. Which sentence can you use before getting on a bus?",
                "q3_opts": [("A", "I need a sandwich now.", False), ("B", "Which bus stops at River Street?", True), ("C", "I like this weather.", False), ("D", "Do you play basketball?", False)],
                "survival": "Which bus stops at River Street?",
                "clue": "printed board",
            },
        },
        {
            "story": "The Library Card",
            "sentences": [
                "At 4:20, Mina entered the old city library.",
                "A small screen near the desk flashed Room 3 closed.",
                "Mina needed a quiet place to call Lina.",
                "She checked her old {rw1} note from yesterday.",
                "Mina saw the word {w1} on a yellow card in one second.",
                "Mina asked the librarian for help.",
                "She asked which room is open now.",
                "The librarian said to check the printed board by the stairs.",
                "The printed board did not show Room 3 at all.",
                "Mina wrote the word {w2} in her notebook.",
                "Lina texted that the online map was changing.",
                "Mina asked for the {rw2} behind this change.",
                "The librarian pointed to Locker 12 near the window.",
                "Mina used the floor map to compare room names.",
                "One label did not match her old {rw3}.",
                "Mina decided to go to Study Room 2.",
                "The door opened and a card fell to the floor.",
                "The card showed a message: You are on the safe side.",
            ],
            "phrases": [
                ("go to", "Phrasal Verb", "前往", "文章用法：Mina decided to go to Study Room 2."),
                ("ask for help", "Phrasal Verb", "寻求帮助", "文章用法：Mina asked the librarian for help."),
                ("printed board", "Collocation", "纸质告示牌", "文章用法：The librarian said to check the printed board by the stairs."),
                ("floor map", "Collocation", "楼层地图", "文章用法：Mina used the floor map to compare room names."),
                ("at all", "Fixed Expression", "根本；完全", "文章用法：The printed board did not show Room 3 at all."),
                ("safe side", "Fixed Expression", "安全的一侧", "文章用法：You are on the safe side."),
            ],
            "quiz": {
                "q1": "1. What did the librarian tell Mina to check?",
                "q1_opts": [("A", "The snack machine", False), ("B", "The printed board", True), ("C", "The bus app", False), ("D", "The weather report", False)],
                "q3": "3. Which sentence can you use to find a room?",
                "q3_opts": [("A", "Which room is open now?", True), ("B", "I lost my umbrella yesterday.", False), ("C", "This cake is very sweet.", False), ("D", "Can you draw a cat?", False)],
                "survival": "Which room is open now?",
                "clue": "printed board",
            },
        },
        {
            "story": "The Market Ticket",
            "sentences": [
                "At 7:15, Mina walked into Pine Night Market.",
                "Two menu boards showed different prices for noodles.",
                "Mina needed to pick up dinner for Lina.",
                "She checked her old {rw1} photo on the phone.",
                "Mina saw the word {w1} on one red ticket in one second.",
                "Mina asked a stall worker for help.",
                "She asked which line is for ticket pickup.",
                "The worker said to check the printed board by the pot.",
                "The printed board did not show combo B at all.",
                "Mina wrote the word {w2} in her notebook.",
                "Lina texted that one menu photo was old.",
                "Mina asked for the {rw2} behind two prices.",
                "The worker pointed to Window 12 near the exit.",
                "Mina used the price list to compare item names.",
                "One item did not match her old {rw3}.",
                "Mina decided to get in line at Window 12.",
                "A new ticket printed and dropped on the counter.",
                "The ticket showed a message: You are on the safe side.",
            ],
            "phrases": [
                ("pick up", "Phrasal Verb", "领取；取餐", "文章用法：Mina needed to pick up dinner for Lina."),
                ("get in line", "Phrasal Verb", "排队", "文章用法：Mina decided to get in line at Window 12."),
                ("price list", "Collocation", "价格表", "文章用法：Mina used the price list to compare item names."),
                ("printed board", "Collocation", "纸质告示牌", "文章用法：The worker said to check the printed board by the pot."),
                ("at all", "Fixed Expression", "根本；完全", "文章用法：The printed board did not show combo B at all."),
                ("safe side", "Fixed Expression", "安全的一侧", "文章用法：You are on the safe side."),
            ],
            "quiz": {
                "q1": "1. What did Mina use to compare item names?",
                "q1_opts": [("A", "A toy map", False), ("B", "The price list", True), ("C", "A train ticket", False), ("D", "A music app", False)],
                "q3": "3. Which sentence can you use at a food stall?",
                "q3_opts": [("A", "Which line is for ticket pickup?", True), ("B", "I forgot my math homework.", False), ("C", "This chair is blue.", False), ("D", "Can fish fly?", False)],
                "survival": "Which line is for ticket pickup?",
                "clue": "price list",
            },
        },
    ]

    return variants[(episode_num - 1) % len(variants)]


def build_episode_draft(episode_num: int, new_words: list[dict], review_words: list[dict]) -> dict:
    rw1, rw2, rw3 = pick_story_review_slots(review_words)

    w1, w2, w3 = [w["word"] for w in new_words]

    variant = pick_story_variant(episode_num)
    substitutions = {
        "rw1": rw1,
        "rw2": rw2,
        "rw3": rw3,
        "w1": w1,
        "w2": w2,
        "w3": w3,
    }
    sentences = [line.format(**substitutions) for line in variant["sentences"]]

    quiz = variant["quiz"].copy()
    quiz["q2"] = f'2. Which word means "{new_words[0].get("chineseMeaning", "含义")}"?'
    quiz["q2_answer"] = new_words[0]["word"]

    tips = (
        f'今天最值得直接背起来的是 <strong>{quiz["survival"]}</strong>，遇到真实场景先开口问。'
        f' 今天也要记住 <strong>{quiz["clue"]}</strong> 这个信息词，查现场英文提示会更稳。'
    )

    return {
        "title": f'{variant["story"]} · Episode {episode_num}',
        "storyName": variant["story"],
        "sentences": sentences,
        "newWords": new_words,
        "reviewWords": review_words,
        "phrases": variant["phrases"],
        "quiz": quiz,
        "tips": tips,
    }


def build_article_html(
    sentences: list[str],
    new_words: list[dict],
    review_words: list[dict],
    phrases: list[tuple[str, str, str, str]],
) -> str:
    vocab_set = {w["word"] for w in new_words}
    review_set = {w.get("word") for w in review_words}

    phrase_map = {
        text: ("phrase-chunk", text, text)
        for text, _, _, _ in phrases
    }

    if "ask for help" in phrase_map:
        phrase_map["asked a worker for help"] = ("phrase-chunk", "ask for help", "asked a worker for help")
        phrase_map["asked the librarian for help"] = ("phrase-chunk", "ask for help", "asked the librarian for help")
        phrase_map["asked a stall worker for help"] = ("phrase-chunk", "ask for help", "asked a stall worker for help")

    def wrap_sentence(idx: int, text: str) -> str:
        rendered = text

        for phrase, (cls, key, show) in phrase_map.items():
            if phrase in rendered:
                rendered = rendered.replace(phrase, f'<span class="{cls}" data-phrase="{key}">{show}</span>', 1)

        for w in vocab_set:
            rendered = re.sub(rf"\\b{re.escape(w)}\\b", f'<span class="vocab-word" data-word="{w}">{w}</span>', rendered, count=1)

        for w in review_set:
            rendered = re.sub(rf"\\b{re.escape(w)}\\b", f'<span class="review-word" data-word="{w}">{w}</span>', rendered, count=1)

        return (
            f'<span class="sent" data-idx="{idx}" data-text="{text}">'
            f'<button class="sent-btn" onclick="playSent(this)" title="播放这句">🔊</button>{rendered}</span>'
        )

    blocks = []
    for i in range(0, len(sentences), 6):
        chunk = sentences[i:i + 6]
        lines = "\n        ".join(wrap_sentence(i + j + 1, s) for j, s in enumerate(chunk))
        blocks.append(f"      <p>\n        {lines}\n      </p>")

    return "\n".join(blocks)


def build_vocab_rows(new_words: list[dict]) -> str:
    rows = []
    for w in new_words:
        rows.append(
            "        <tr>\n"
            f"          <td><strong>{w['word']}</strong></td>\n"
            f"          <td><span class=\"pos-badge\">{w.get('partOfSpeech', 'n.')}</span></td>\n"
            f"          <td><div class=\"zh-meaning\">{w.get('chineseMeaning', '')}</div><div class=\"example-sent\">{w.get('exampleSentence', '')}</div></td>\n"
            "        </tr>"
        )
    return "\n".join(rows)


def build_phrase_items(phrases: list[tuple[str, str, str, str]]) -> str:
    return "\n".join(
        "      <div class=\"phrase-item\">\n"
        f"        <div class=\"ph-text\">{text}</div>\n"
        f"        <div class=\"ph-zh\">{zh}</div>\n"
        f"        <div class=\"ph-note\">类型：{ptype}｜{note}</div>\n"
        "      </div>"
        for text, ptype, zh, note in phrases
    )


def build_quiz_block(quiz: dict) -> str:
    q1_opts = "\n".join(
        f"        <div class=\"quiz-option\" onclick=\"answer(this,'{'correct' if is_ok else 'wrong'}')\"><span class=\"opt-key\">{label}</span>{text}</div>"
        for label, text, is_ok in quiz["q1_opts"]
    )
    q2_opts = "\n".join([
        f"        <div class=\"quiz-option\" onclick=\"answer(this,'correct')\"><span class=\"opt-key\">A</span>{quiz['q2_answer']}</div>",
        "        <div class=\"quiz-option\" onclick=\"answer(this,'wrong')\"><span class=\"opt-key\">B</span>history</div>",
        "        <div class=\"quiz-option\" onclick=\"answer(this,'wrong')\"><span class=\"opt-key\">C</span>ticket</div>",
        "        <div class=\"quiz-option\" onclick=\"answer(this,'wrong')\"><span class=\"opt-key\">D</span>driver</div>",
    ])
    q3_opts = "\n".join(
        f"        <div class=\"quiz-option\" onclick=\"answer(this,'{'correct' if is_ok else 'wrong'}')\"><span class=\"opt-key\">{label}</span>{text}</div>"
        for label, text, is_ok in quiz["q3_opts"]
    )

    return (
        "    <div class=\"quiz-q\">\n"
        f"      <div class=\"quiz-question\">{quiz['q1']}</div>\n"
        "      <div class=\"quiz-options\">\n"
        f"{q1_opts}\n"
        "      </div>\n"
        "    </div>\n"
        "    <div class=\"quiz-q\">\n"
        f"      <div class=\"quiz-question\">{quiz['q2']}</div>\n"
        "      <div class=\"quiz-options\">\n"
        f"{q2_opts}\n"
        "      </div>\n"
        "    </div>\n"
        "    <div class=\"quiz-q\">\n"
        f"      <div class=\"quiz-question\">{quiz['q3']}</div>\n"
        "      <div class=\"quiz-options\">\n"
        f"{q3_opts}\n"
        "      </div>\n"
        "    </div>\n"
        "    <button class=\"answers-btn\" onclick=\"toggleAnswers()\">显示答案</button>\n"
        "    <div class=\"answers-reveal\" id=\"answers-reveal\">\n"
        "      ✅ &nbsp;Q1: <strong>B</strong> &nbsp;｜&nbsp; Q2: <strong>A</strong> &nbsp;｜&nbsp; Q3: <strong>B</strong>\n"
        "    </div>"
    )


def build_vocab_js(new_words: list[dict]) -> str:
    lines = []
    for w in new_words:
        lines.append(
            f"    '{w['word']}': {{ pos:'{w.get('partOfSpeech', 'n.')}', zh:'{w.get('chineseMeaning', '')}', example:'{w.get('exampleSentence', '')}' }},"
        )
    return "\n".join(lines)


def build_review_js(review_words: list[dict]) -> str:
    lines = []
    for w in review_words[:3]:
        lines.append(
            f"    '{w.get('word', '')}': {{ pos:'{w.get('partOfSpeech', '')}', zh:'{w.get('chineseMeaning', '')}', example:'{w.get('exampleSentence', '')}' }},"
        )
    if not lines:
        lines.append("    'history': { pos:'n.', zh:'历史；记录', example:'Check the route history before you go.' },")
    return "\n".join(lines)


def ensure_audio_speed_controls(html: str) -> str:
    speed_css = (
        "    .speed-mode { display: inline-flex; align-items: center; gap: .4rem; margin-left: .35rem; }\n"
        "    .speed-mode-label { font-family: sans-serif; font-size: .78rem; font-weight: 700; opacity: .85; }\n"
        "    .speed-mode-group { display: inline-flex; align-items: center; gap: .2rem; padding: .2rem; background: rgba(255,255,255,.18); border-radius: 99px; }\n"
        "    .audio-speed-btn { border: none; background: transparent; color: white; border-radius: 99px; padding: .26rem .68rem; font-family: sans-serif; font-size: .74rem; font-weight: 700; cursor: pointer; transition: all .15s; }\n"
        "    .audio-speed-btn:hover { background: rgba(255,255,255,.2); }\n"
        "    .audio-speed-btn.active { background: rgba(255,255,255,.92); color: #4f7cff; }"
    )

    if ".audio-speed-btn" not in html:
        html = re.sub(r"(\s*\.loop-btn\.active \{[^\n]*\}\n)", r"\1" + speed_css + "\n", html, count=1)

    controls_block = (
        "<div class=\"player-controls\">\n"
        "      <button class=\"loop-btn\" onclick=\"toggleLoop(this)\">🔁 循環播放</button>\n"
        "      <span class=\"speed-mode\" role=\"group\" aria-label=\"播放速度\">\n"
        "        <span class=\"speed-mode-label\">速度</span>\n"
        "        <span class=\"speed-mode-group\">\n"
        "          <button type=\"button\" class=\"audio-speed-btn\" data-speed=\"0.7\" onclick=\"setAudioSpeed(0.7, this)\">超慢速</button>\n"
        "          <button type=\"button\" class=\"audio-speed-btn active\" data-speed=\"0.85\" onclick=\"setAudioSpeed(0.85, this)\">慢速</button>\n"
        "          <button type=\"button\" class=\"audio-speed-btn\" data-speed=\"1\" onclick=\"setAudioSpeed(1, this)\">中速</button>\n"
        "          <button type=\"button\" class=\"audio-speed-btn\" data-speed=\"1.2\" onclick=\"setAudioSpeed(1.2, this)\">快速</button>\n"
        "        </span>\n"
        "      </span>\n"
        "    </div>"
    )
    html = re.sub(r"<div class=\"player-controls\">[\s\S]*?</div>", controls_block, html, count=1)

    if "let currentAudioSpeed" in html:
        html = re.sub(r"let currentAudioSpeed = [0-9.]+;", "let currentAudioSpeed = 0.85;", html, count=1)
    else:
        html = re.sub(
            r"(let sentencePlaybackMode = 'once';\n)",
            r"\1  let currentAudioSpeed = 0.85;\n",
            html,
            count=1,
        )

    if "AUDIO_SPEED_STORAGE_KEY" not in html:
        html = re.sub(
            r"(let currentAudioSpeed = [0-9.]+;\n)",
            r"const AUDIO_SPEED_STORAGE_KEY = 'audio_speed_pref';\n  const AUDIO_SPEED_OPTIONS = [0.7, 0.85, 1, 1.2];\n  \1",
            html,
            count=1,
        )

    if "function setAudioSpeed(" not in html:
        speed_js = (
            "\n  function syncAudioSpeedButtons() {\n"
            "    document.querySelectorAll('.audio-speed-btn').forEach(btn => {\n"
            "      btn.classList.toggle('active', Number(btn.dataset.speed) === currentAudioSpeed);\n"
            "    });\n"
            "  }\n"
            "\n"
            "  function setAudioSpeed(speed, clickedBtn) {\n"
            "    currentAudioSpeed = Number(speed) || 1;\n"
            "    const articleAudio = document.getElementById('article-audio');\n"
            "    if (articleAudio) articleAudio.playbackRate = currentAudioSpeed;\n"
            "    sentAudio.playbackRate = currentAudioSpeed;\n"
            "\n"
            "    if (clickedBtn) {\n"
            "      document.querySelectorAll('.audio-speed-btn').forEach(btn => btn.classList.remove('active'));\n"
            "      clickedBtn.classList.add('active');\n"
            "    } else {\n"
            "      syncAudioSpeedButtons();\n"
            "    }\n"
            "  }\n"
        )
        html = re.sub(r"\n\s*function setSentenceMode\(mode\) \{", speed_js + "\n  function setSentenceMode(mode) {", html, count=1)

    if "localStorage.setItem(AUDIO_SPEED_STORAGE_KEY" not in html:
        html = re.sub(
            r"(currentAudioSpeed = Number\(speed\) \|\| 1;\n)",
            r"\1    localStorage.setItem(AUDIO_SPEED_STORAGE_KEY, String(currentAudioSpeed));\n",
            html,
            count=1,
        )

    if "sentAudio.playbackRate = currentAudioSpeed;" not in html:
        html = re.sub(
            r"(\n\s*sentAudio\.loop = sentencePlaybackMode === 'loop';)",
            r"\1\n    sentAudio.playbackRate = currentAudioSpeed;",
            html,
            count=1,
        )

    html = re.sub(
        r"articleAudio\.src = articleSrc;\n\s*articleAudio\.preload = 'metadata';\n\s*articleAudio\.load\(\);",
        "articleAudio.src = articleSrc;\n    articleAudio.playbackRate = currentAudioSpeed;\n    articleAudio.preload = 'metadata';\n    articleAudio.load();\n    articleAudio.playbackRate = currentAudioSpeed;",
        html,
        count=1,
    )

    if "const savedSpeed = Number(localStorage.getItem(AUDIO_SPEED_STORAGE_KEY));" not in html:
        html = re.sub(
            r"(document\.addEventListener\('DOMContentLoaded', async \(\) => \{\n)",
            r"\1    const savedSpeed = Number(localStorage.getItem(AUDIO_SPEED_STORAGE_KEY));\n    if (AUDIO_SPEED_OPTIONS.includes(savedSpeed)) {\n      currentAudioSpeed = savedSpeed;\n    }\n\n",
            html,
            count=1,
        )

    if "syncAudioSpeedButtons();" not in html:
        html = re.sub(r"(\n\s*syncSentenceModeButtons\(\);)", r"\1\n    syncAudioSpeedButtons();", html, count=1)

    return html


def ensure_home_button(html: str) -> str:
    home_css = (
        "    .home-btn-wrap { display: flex; justify-content: center; margin-bottom: .8rem; }\n"
        "    .home-btn { display: inline-flex; align-items: center; gap: .45rem; padding: .55rem 1.1rem; border-radius: 999px; border: 1.5px solid var(--accent); background: white; color: var(--accent); font-family: sans-serif; font-size: .86rem; font-weight: 700; text-decoration: none; transition: all .15s; }\n"
        "    .home-btn:hover { background: var(--accent); color: white; }"
    )

    if ".home-btn-wrap" not in html:
        html = re.sub(r"(\s*\.audio-speed-btn\.active \{[^\n]*\}\n)", r"\1" + home_css + "\n", html, count=1)

    if "class=\"home-btn-wrap\"" not in html:
        home_block = (
            "  <div class=\"home-btn-wrap\">\n"
            "    <a class=\"home-btn\" href=\"../../index.html\" aria-label=\"返回首页\">🏠 返回首页</a>\n"
            "  </div>\n\n"
        )
        html = re.sub(r"(<div class=\"header\">)", home_block + r"\1", html, count=1)

    return html


def apply_episode_to_html(base_html: str, today: str, day_num: int, draft: dict) -> str:
    article_html = build_article_html(draft["sentences"], draft["newWords"], draft["reviewWords"], draft["phrases"])
    vocab_rows = build_vocab_rows(draft["newWords"])
    phrase_items = build_phrase_items(draft["phrases"])
    quiz_block = build_quiz_block(draft["quiz"])
    vocab_js = build_vocab_js(draft["newWords"])
    review_js = build_review_js(draft["reviewWords"])

    title = f"Daily English · {today}"
    parsed = datetime.strptime(today, "%Y-%m-%d")
    month_day = parsed.strftime("%B %d, %Y").replace(" 0", " ")

    html = base_html
    html = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", html, flags=re.S)
    html = re.sub(r"<div class=\"date-badge\">.*?</div>", f"<div class=\"date-badge\">{month_day} · Day {day_num}</div>", html, count=1, flags=re.S)
    html = re.sub(r"<h1>[\s\S]*?</h1>", f"<h1><span>{draft['storyName']}</span> · Episode {draft['title'].split()[-1]}</h1>", html, count=1)
    html = re.sub(r"<div class=\"player-title\">.*?</div>", f"<div class=\"player-title\">{draft['title']}</div>", html, count=1, flags=re.S)

    html = re.sub(
        r"<div class=\"article-body\" id=\"article-body\">[\s\S]*?</div>\s*</div>\s*\n\s*<div class=\"card\">\s*\n\s*<div class=\"card-title\">📚 New Words Today</div>",
        f"<div class=\"article-body\" id=\"article-body\">\n{article_html}\n    </div>\n  </div>\n\n  <div class=\"card\">\n    <div class=\"card-title\">📚 New Words Today</div>",
        html,
        count=1,
    )

    html = re.sub(r"<tbody>[\s\S]*?</tbody>", f"<tbody>\n{vocab_rows}\n      </tbody>", html, count=1)
    html = re.sub(r"<div class=\"phrase-list\">[\s\S]*?</div>\s*</div>\s*\n\s*<div class=\"card\">\s*\n\s*<div class=\"card-title\">✏️ Quiz</div>",
                  f"<div class=\"phrase-list\">\n{phrase_items}\n    </div>\n  </div>\n\n  <div class=\"card\">\n    <div class=\"card-title\">✏️ Quiz</div>",
                  html,
                  count=1)

    html = re.sub(r"<div class=\"card-title\">✏️ Quiz</div>[\s\S]*?<div class=\"card\">\s*\n\s*<div class=\"card-title\">🧠 Active Recall Quiz</div>",
                  f"<div class=\"card-title\">✏️ Quiz</div>\n{quiz_block}\n  </div>\n\n  <div class=\"card\">\n    <div class=\"card-title\">🧠 Active Recall Quiz</div>",
                  html,
                  count=1)

    tips = draft["tips"]
    html = re.sub(r"<div class=\"tips-box\">[\s\S]*?</div>", f"<div class=\"tips-box\">{tips}</div>", html, count=1)

    html = re.sub(r"const VOCAB = \{[\s\S]*?\};", f"const VOCAB = {{\n{vocab_js}\n  }};", html, count=1)
    html = re.sub(r"const REVIEW = \{[\s\S]*?\};", f"const REVIEW = {{\n{review_js}\n  }};", html, count=1)

    phrase_js_lines = []
    for text, ptype, zh, note in draft["phrases"]:
        safe_text = text.replace("'", "\\\\'")
        safe_zh = zh.replace("'", "\\\\'")
        safe_note = note.replace("'", "\\\\'")
        safe_type = ptype.replace("'", "\\\\'")
        phrase_js_lines.append(
            f"    '{safe_text}': {{ zh:'{safe_zh}', note:'{safe_note}', type:'{safe_type}' }},"
        )

    phrase_js = "const PHRASES = {\n" + "\n".join(phrase_js_lines) + "\n  };"
    html = re.sub(r"const PHRASES = \{[\s\S]*?\};", phrase_js, html, count=1)
    html = ensure_audio_speed_controls(html)
    html = ensure_home_button(html)

    return html


async def generate_audio(folder: Path, sentences: list[str]) -> None:
    import edge_tts
    import edge_tts.communicate as communicate

    if hasattr(communicate, "_SSL_CTX") and communicate._SSL_CTX:
        communicate._SSL_CTX.check_hostname = False
        communicate._SSL_CTX.verify_mode = ssl.CERT_NONE

    voice = "en-US-JennyNeural"
    rate = "-10%"

    async def save_one(text: str, output_path: Path) -> None:
        tts = edge_tts.Communicate(text, voice=voice, rate=rate)
        await tts.save(str(output_path))

    article_text = " ".join(sentences)
    await save_one(article_text, folder / "article.mp3")

    for idx, sentence in enumerate(sentences, start=1):
        await save_one(sentence, folder / f"s{idx:02d}.mp3")


def generate_today_pipeline(repo_root: Path) -> dict:
    daily_dir = repo_root / "daily"
    if not daily_dir.exists():
        raise FileNotFoundError("daily directory not found")

    today = datetime.now().strftime("%Y-%m-%d")
    today_dir = daily_dir / today
    today_dir.mkdir(parents=True, exist_ok=True)

    profile_path = repo_root / "profile.json"
    learning_path = repo_root / "vocabulary" / "learning.json"
    ket_path = repo_root / "vocabulary" / "ket_pool.json"

    profile = json.loads(profile_path.read_text(encoding="utf-8"))
    learning = json.loads(learning_path.read_text(encoding="utf-8"))
    ket = json.loads(ket_path.read_text(encoding="utf-8"))

    learning_words = learning.get("words", [])
    ket_words = ket.get("words", [])

    if profile.get("lastUpdated") != today:
        profile["totalDays"] = int(profile.get("totalDays", 0)) + 1
        profile["currentEpisode"] = int(profile.get("currentEpisode", 0)) + 1
        profile["lastUpdated"] = today

    episode_num = int(profile.get("currentEpisode", 0))
    day_num = int(profile.get("totalDays", 0))

    today_index = today_dir / "index.html"
    copied_from = None

    if not today_index.exists():
        dates = list_date_folders(daily_dir)
        source_date = next((d for d in dates if d != today), None)
        if not source_date:
            raise FileNotFoundError("No template page found in daily directory")
        source_index = daily_dir / source_date / "index.html"
        today_index.write_text(source_index.read_text(encoding="utf-8"), encoding="utf-8")
        copied_from = source_date

    new_words = choose_new_words(ket_words, learning_words)
    review_words = find_due_review_words(learning_words, today, count=3)
    draft = build_episode_draft(episode_num, new_words, review_words)

    base_html = today_index.read_text(encoding="utf-8")
    new_html = apply_episode_to_html(base_html, today, day_num, draft)
    today_index.write_text(new_html, encoding="utf-8")

    existing = {w.get("word", "").lower() for w in learning_words}
    for nw in new_words:
        if nw["word"].lower() in existing:
            continue
        learning_words.append(
            {
                "word": nw["word"],
                "partOfSpeech": nw.get("partOfSpeech", "n."),
                "chineseMeaning": nw.get("chineseMeaning", ""),
                "exampleSentence": nw.get("exampleSentence", ""),
                "dateAdded": today,
                "reviewCount": 0,
                "nextReview": (datetime.now().date() + timedelta(days=1)).strftime("%Y-%m-%d"),
                "lastReviewedDate": None,
            }
        )

    profile_path.write_text(json.dumps(profile, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    learning_path.write_text(json.dumps(learning, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    asyncio.run(generate_audio(today_dir, draft["sentences"]))

    return {
        "today": today,
        "sentenceCount": len(draft["sentences"]),
        "copiedFrom": copied_from,
        "episode": episode_num,
        "newWords": [w["word"] for w in new_words],
        "indexPath": f"daily/{today}/index.html",
        "audioPath": f"daily/{today}/article.mp3",
    }


class AppHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, directory=None, **kwargs):
        self.repo_root = Path(directory).resolve() if directory else Path.cwd().resolve()
        super().__init__(*args, directory=str(self.repo_root), **kwargs)

    def _send_json(self, payload: dict, status: int = HTTPStatus.OK) -> None:
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path == "/__health":
            self._send_json({"ok": True, "service": "local_server", "root": str(self.repo_root)})
            return

        super().do_GET()

    def do_POST(self):
        if self.path != "/__generate_today":
            self._send_json({"ok": False, "error": "Not Found"}, status=HTTPStatus.NOT_FOUND)
            return

        # Drain body if present.
        content_length = int(self.headers.get("Content-Length", "0") or 0)
        if content_length > 0:
            _ = self.rfile.read(content_length)

        try:
            result = generate_today_pipeline(self.repo_root)
            self._send_json({"ok": True, "result": result})
        except Exception as exc:
            self._send_json({"ok": False, "error": str(exc)}, status=HTTPStatus.INTERNAL_SERVER_ERROR)


def run_server(repo_root: Path, port: int) -> None:
    handler = lambda *args, **kwargs: AppHandler(*args, directory=str(repo_root), **kwargs)
    server = ThreadingHTTPServer(("", port), handler)
    print(f"Serving on http://localhost:{port}/")
    print(f"Generate endpoint: http://localhost:{port}/__generate_today")
    server.serve_forever()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Local server with daily page/audio generation endpoint")
    parser.add_argument("--port", type=int, default=8080)
    parser.add_argument("--root", type=str, default=str(Path(__file__).resolve().parent))
    args = parser.parse_args()

    root = Path(args.root).resolve()
    run_server(root, args.port)
