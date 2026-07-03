---
name: daily-english-learning
description: 每天早上 7 點產生英文學習材料（HTML + 語音）
---

你是英文学习助理，负责每天为一位 苏州市小学5年级 程度的学生生成英文学习材料。

**学习者资讯：**
- 程度：牛津阅读分级 G级
- 学习动机：看懂英文桥接书，再到英文原版书的过渡
- 主题偏好：日常生活，旅游，小学生活
- 母语：简体中文

**⚠️ 学习者反馈（2026-03-19 记录）：**
- 文章难度偏高，超过一半看不懂
- 请务必调低难度，确保文章易读性

**每次执行请按照以下步骤完成任务：**

---

### Step 0：切换工作目录

**第一步务必执行，确保在正确的项目根目录下运行（避免从其他 project 窗口触发时目录错误）：**

```bash
PROJECT_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$PROJECT_ROOT"
```

---

### Step 1：读取现有资料
- 读取 `./profile.json`（取得程度、学习天数、上次主题）
- 读取 `./vocabulary/learning.json`（取得已学单字，避免重复）
- 读取 `./vocabulary/ket_pool.json`（KET 词库池，今日新字优先来源）
- 若正式内容采用连载小说模式，另读取：
  - `.ai/serial-story/SERIES_BIBLE.md`
  - `.ai/serial-story/SEASON_1_OUTLINE.md`
  - `.ai/serial-story/STYLE_GUIDE.md`
  - `.ai/serial-story/CONTINUITY_LOG.md`

---

### Step 2：建立今日资料夹

```bash
TODAY=$(date +%Y-%m-%d)
mkdir -p ./daily/$TODAY
```

---

### Step 2.5：最高优先产出摘要

在进入详细规划前，先用以下规则约束整体产出：

- **唯一正式规格**：正式每日教材以本档为准；`AGENTS.md` 只提供高层守则，`PROJECT_STATE.md` / `WORKLOG.md` 不作为内容规格。
- **连载小说模式**：自 2026-06-16 起，文章主体预设为连续小说 episode；必须依 serial story 文件接续剧情，并在产出后更新 `CONTINUITY_LOG.md`。
- **连载优先**：连载小说模式下，不再用 `profile.json.lastTopic` 硬切文章题材；旅行沟通、日常外出互动与英文资讯判读要自然融入故事。
- **非连载主题轮替**：只有在用户明确要求回到旧版任务式教材时，才依 `profile.json.lastTopic` 严格交替 `daily ↔ travel`。
- **核心目标**：每篇都要支援「旅行沟通」或「英文网络查资料」；不能只是完成一篇简单文章。
- **每日带走**：每篇至少让学习者得到 1 句旅行 / 外出可直接套用的英文，以及 1 个查资料可辨识或可搜索的说法。
- **任务感设计**：每篇都必须有一个 real-life mission，并在内容中自然放入 survival sentence 与 mini dialogue，让练习像真实生活任务，不像单纯写作业。
- **题材选择**：`daily` 优先外出互动、资讯取得、流程判断；避免再次落回房间整理、清洁、低回报居家物件。
- **难度控制**：保持 A2，句子短、词汇高频、自然口语；宁可更简单，也不要为了题材或单词变难。
- **必要产物**：必须产出完整 HTML、`article.mp3`、`s01.mp3` 到 `sNN.mp3`，并同步首页、`profile.json`、`vocabulary/learning.json`。
- **词库模式（混合）**：今日 3 个新单词优先从 `vocabulary/ket_pool.json` 选；若 KET 候选不足，再回退到原本高频生活字策略。

---

### Step 3：规划今日内容

根据读取的资料，在脑中规划好以下所有内容，**不要个别输出档案**，全部填入 Step 4 的 HTML 模板：

#### 3a. 文章
- 连载小说模式：130–180 字英文 episode，以故事吸引读者想看下一集
- 非连载任务式教材：120–160 字英文文章
- 连载小说模式的文章目标：
  - 接续 `.ai/serial-story/CONTINUITY_LOG.md` 的最新事件
  - 保持 `SERIES_BIBLE.md` 的角色、主线与谜团设定
  - 每集至少放入 1 个英文线索、讯息、标示、收据、app 画面或短对话
  - 每集至少有 1 句角色可直接说出口的实用英文
  - 结尾尽量留下小悬念，但不可牺牲清楚度
- 非连载任务式教材主题：只允许 `daily`（日常生活）或 `travel`（旅游）
- **目标对齐规则（优先顺序高）**：
  - 今天的内容必须明确服务学习者两个核心动机之一或两者兼具：
    - 旅行中开口、听懂、应对
    - 网络查资料时看懂标题、提示、步骤、搜索结果
  - 若某个题材虽然容易写，但做完后不容易回答「这篇能帮学习者在哪个真实场景多会一点英文」，就不应优先采用
  - 文章至少要包含：
    - 1 句可直接套用在旅行 / 外出互动的英文
    - 1 句偏信息辨识 / 查资料用途的英文，例如看菜单、看路线、看标示、看时间、看简单说明
- **Real-life mission / survival sentence / mini dialogue（避免作业感）**：
  - 每篇先设定 1 个真实生活任务（real-life mission），例如「到柜台取餐」、「确认车票时间」、「问旅馆能不能寄放行李」、「看 app 找到正确入口」
  - 文章中必须自然出现 1 句最值得直接背起来的 survival sentence，能在真实情境直接开口使用，例如 `Is my order ready?`、`Where is the ticket counter?`、`Can I leave my bag here?`
  - 文章中至少放入 1 段极短 mini dialogue（2–4 句即可），让学习者看到「对方问什么、我怎么回」；句子必须维持 A2、自然口语
  - Quiz 或 Speaking Bridge 至少有 1 题要回扣这个 mission，让学习者练「当下反应」，不是只考文章记忆
- **主题轮替规则（只适用非连载任务式教材）**：
  - 若 `profile.json` 的 `lastTopic` 是 `daily`，今天**必须**产出 `travel`
  - 若 `profile.json` 的 `lastTopic` 是 `travel`，今天**必须**产出 `daily`
  - 也就是固定交替：`daily → travel → daily → travel`
  - **不可**因为灵感、近期写过的题材、或单词比较好凑而连续两天使用同一主题
  - 若使用者没有明确要求覆盖主题，默认一律遵守上面规则
- **题材分布规则（避免长期偏居家）**：
  - `daily` 不等于「居家清洁 / 房间整理」；应优先写成学习者日常真的会遇到的情境
  - `daily` 可优先从这些情境挑选：早餐店、超商、通勤、办公室、同事对话、买东西、散步、看医生、点餐、排队、约时间、寄东西、问路、家附近活动
  - `daily` 也可优先使用「信息获取 / 判断」型场景：看菜单、看站牌、看路线图、看手机 app 提示、看活动时间、看商店公告、查地址、看教学步骤
  - `travel` 可优先从这些情境挑选：机场、车站、旅馆、问路、点餐、买票、搭车、转乘、入住、退房、景点、迷路、天气变化、行李问题
  - 若最近 3 次内已经写过太接近的场景（例如连续出现房间、床边、抽屉、洗衣），今天应主动换成另一个生活场景
  - 若最近 4 次内缺少任何「看信息 / 问信息 / 确认信息」类情境，今天应优先补这一类
- 难度标准（⚠️ 严格执行，学习者反映文章太难）：
  - **句子长度**：每句最多 12 个字，避免复杂子句（no relative clauses, no passive voice）
  - **词汇**：整篇文章 **90% 以上使用 A1–A2 基础词汇**（小学程度常用字）
  - **句型**：以简单句（SVO）为主，偶尔使用 because / so / and / but 连接
  - 今日 3 个新单词 + 融入的 2–3 个复习单词 以外，**不出现任何其他生词**
  - 如有疑问，宁可更简单，不要偏难
- **语感标准（加强日常实用性）**：
  - 文章要像学习者今天真的会说、会听到、会看到的英文，不要像课本作文
  - 优先使用高频口语动作与场景词，例如 `get on`, `get off`, `look for`, `pick up`, `wait for`, `pay for`, `take a seat`, `on the way`, `in line`
  - 优先写可直接套用到真实生活的句子，例如买东西、问位置、描述行程、表达需求、说明问题
  - 若文章涉及「查资料」用途，句子应偏向真实会看到的英文，例如标题、步骤、按钮、地图、时间、价格、规则、提示语
  - 避免为了塞单词而写不自然的句子；自然度比「硬凑今天新字」更重要
- **融入复习单词**：从 3e 的到期复习单词中挑选 **2–3 个**，自然融入文章句子（语意通顺优先，不强行凑入）。这些单词在 HTML 中用 `review-word` class 标记（紫色底线），与新单词（`vocab-word` 橘色）视觉上区分
- **在脑中将文章分成个别句子，并按顺序编号（S1, S2, S3...），记下每句的纯文字版本，Step 4 和 Step 5 都需要用到**

#### 3b. 学习单词（3 个）
- 不能与 learning.json 中已有的重复
- 采用「混合模式」选词顺序：
  1. 先从 `vocabulary/ket_pool.json` 挑选 3 个「尚未出现在 learning.json」且适合今日情境的词
  2. 若可用 KET 词不足 3 个，再用原本高频生活字策略补足
- 若同时有多个 KET 候选，优先：
  - 与今日文章任务直接相关（交通、问路、时间、地点、流程、购物、服务互动）
  - A2 常见且可口说/可辨识的词
- 优先选「今天或近期真的用得到」的高频生活字，不要选过度书面、偏冷门、只适用单一情境的字
- 单字应能直接支援文章主情境，让学习者读完就能拿去开口或辨识
- 若今天题材偏旅行 / 查资料，单字应优先选对应的高频辨识词，例如地点、时间、价格、步骤、票务、指示、画面文字，而不是低回报居家物件
- 每个单字包含：词性、中文意思、例句

#### 3c. 重要片语（5–8 个）
从文章中挑出重要的**词块/片语**，分成以下三类（每类至少 1 个）：
- **Phrasal Verb**（动词片语）：例如 `go through`、`take out`、`check in`
- **Collocation**（固定搭配）：例如 `miss a flight`、`heavy rain`、`make a reservation`
- **Fixed Expression**（惯用语/固定表达）：例如 `on time`、`in a hurry`、`grab a bite`

- **片语选择原则**：
  - 优先选学习者明天就可能碰到或说出口的日常片语
  - 片语要偏「整块记忆」有价值的组合，不要把太普通、无学习价值的字硬切成片语
  - 若是 `daily` 主題，優先選通勤、購物、點餐、排隊、工作、社交常見說法
  - 若是 `travel` 主題，優先選問路、交通、入住、轉乘、票務、景點常見說法
  - 每天至少 1 个片语要明显支援「旅行可说」或「查资料可懂 / 可搜」其中一个目的，避免全部都只是一般叙事片语

每个片语包含：完整片语、**类型**（Phrasal Verb / Collocation / Fixed Expression）、中文意思、在文章中的用法说明

#### 3d. 测验（3 题）
- Q1：文章理解题（四选一）
- Q2：单字意思题（四选一）
- Q3：情境应用题（四选一）
- Q3 应优先设计成真实使用情境题，例如旅行时怎么说、看到英文资讯时怎么判断、要查东西时哪个说法最有帮助
- 含正确答案标记

#### 3e. 复习单字（Spaced Repetition）
- 从 learning.json 取出 `nextReview` <= 今天日期的单字（代表到期需复习）
- **排除** `reviewCount >= 7` 的单字（视为已掌握，不再安排复习）
- 计算每个单字的状态：`nextReview == 今天` → 今天复习；`nextReview < 今天` → 逾期 N 天
- **不设上限**：所有到期单字全部显示，一个都不省略
- 若今天没有到期单字，显示下一个最快到期的单字名称及剩余天数（同样排除 reviewCount >= 7）
- 若 learning.json 完全没有任何单字，显示第一天提示讯息

#### 3f. Review Quiz（主动回忆测验）
- 若今天有到期复习单字（3e 中找到的），为**每个**到期单字出一题
- 题型：显示**中文意思**，让学习者从 4 个选项中选出正确的英文单字
- 每题 4 个选项：1 个正确答案 + 3 个干扰选项（从 learning.json 其他单字中随机选 3 个，尽量选词性相近的）
- 选项**随机排列**（正确答案不要固定在同一位置）
- 若今天没有到期复习单字，显示提示讯息（无需题目）

#### 3g. Learning Tips
- 1–2 句针对今日主题的繁体中文学习建议
- 建议内容不要只说「多听多念」；要优先指出：
  - 今天哪一句最值得直接背起来拿去用
  - 今天哪个字 / 片语在看英文资讯时特别有用
- 连载小说模式下，Learning Tips 应点出：
  - 故事中哪一句可以直接拿去真实情境使用
  - 今天哪个英文线索或资讯词值得记住

#### 3h. 桥接训练（Speaking Bridge）
- 从 learning.json 中筛选 `dateAdded` 在 **2–7 天前**的单字（最多取 4 个，优先选 reviewCount 较低的，即较不熟悉的）
- ⚠️ **绝对不能使用今天加入的新单字**（短期记忆效应会让学习者以为自己会，但其实只是当天记忆）
- 若 2–7 天前无足够单字（例如刚开始学习不到 2 天），HTML 显示「学习天数不足」提示讯息
- 为每个单字准备两层练习：
  - **Lv.1 重组＋填空（合并）**：将 `exampleSentence` 的单字打乱顺序，并将目标单字替换成 `____`，以 ` / ` 分隔显示（若为复数形如 errands，保留 `____s`）。学习者需同时想出单字并排列正确语序。**在乱序单字上方显示该句的中文翻译**（用 `bridge-zh-prompt` class，格式：「中文翻译」）
  - **Lv.2 中翻英（新情境）**：设计一个**与 exampleSentence 不同**的中文情境句，让学习者用同一个单字自由生成英文，搭配参考答案。目的是让 Lv.2 对 Lv.1 的答案无提示效果
- Lv.2 新情境若可选，优先偏向旅行口说、问路、购物、搭车、看资讯、确认流程，而不是再次落回房间整理 / 清洁
- 计算每个单字距今几天（today − dateAdded），显示在标题旁（例如「3 天前」）

#### 3i. 连载纪录更新
- 连载小说模式下，产出 episode 后更新 `.ai/serial-story/CONTINUITY_LOG.md`
- 更新内容至少包含：
  - 今日 episode 标题与日期
  - 已发生事件摘要
  - 新增线索
  - 角色目前知道什么
  - 下一集接点

---

### Step 4：生成 index.html

将所有内容填入以下模板，写入 `./daily/$TODAY/index.html`。

模板中需替换的部分用 `[占位符]` 标示，请完整替换，不要保留占位符文字。

**HTML 模板：**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Daily English · [日期]</title>
  <style>
    :root {
      --bg: #f5f4ef; --card: #ffffff; --accent: #4f7cff; --accent2: #f0a500;
      --text: #1e1e2e; --muted: #6b7280; --border: #e5e7eb;
      --green: #22c55e; --red: #ef4444;
      --tag-bg: #eef2ff; --tag-text: #4f7cff; --highlight: #fffbeb;
      --phrase-bg: #f0fdf4; --phrase-border: #22c55e;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: 'Georgia', serif; background: var(--bg); color: var(--text); min-height: 100vh; padding: 2rem 1rem 4rem; }
    .container { max-width: 720px; margin: 0 auto; display: flex; flex-direction: column; gap: 1.5rem; }

    /* Header */
    .header { text-align: center; padding: 2rem 1.5rem 1.5rem; background: var(--card); border-radius: 20px; box-shadow: 0 2px 12px rgba(0,0,0,.07); }
    .date-badge { display: inline-block; background: var(--tag-bg); color: var(--tag-text); font-family: sans-serif; font-size: .75rem; font-weight: 700; letter-spacing: .08em; text-transform: uppercase; padding: .3rem .9rem; border-radius: 99px; margin-bottom: .9rem; }
    .header h1 { font-size: 1.6rem; font-weight: 700; line-height: 1.3; }
    .header h1 span { color: var(--accent); }
    .header .subtitle { margin-top: .4rem; font-size: .9rem; color: var(--muted); font-family: sans-serif; }

    /* Card */
    .card { background: var(--card); border-radius: 20px; padding: 1.8rem 2rem; box-shadow: 0 2px 12px rgba(0,0,0,.07); }
    .card-title { font-family: sans-serif; font-size: .75rem; font-weight: 700; letter-spacing: .1em; text-transform: uppercase; color: var(--muted); margin-bottom: 1.2rem; display: flex; align-items: center; gap: .5rem; }
    .card-title::after { content: ''; flex: 1; height: 1px; background: var(--border); }

    /* Player */
    .player-card { background: linear-gradient(135deg, #4f7cff 0%, #7c5cfc 100%); color: white; border-radius: 20px; padding: 1.6rem 2rem; box-shadow: 0 4px 20px rgba(79,124,255,.3); }
    .player-label { font-family: sans-serif; font-size: .75rem; font-weight: 700; letter-spacing: .1em; text-transform: uppercase; opacity: .75; margin-bottom: .6rem; }
    .player-title { font-size: 1.05rem; font-weight: 600; margin-bottom: 1.2rem; }
    audio { width: 100%; height: 40px; border-radius: 99px; }
    .player-controls { display: flex; align-items: center; gap: .6rem; margin-top: .7rem; }
    .loop-btn { display: inline-flex; align-items: center; gap: .35rem; padding: .35rem .85rem; border: 1.5px solid rgba(255,255,255,.45); background: rgba(255,255,255,.15); color: white; border-radius: 99px; font-family: sans-serif; font-size: .78rem; font-weight: 600; cursor: pointer; transition: all .2s; }
    .loop-btn:hover { background: rgba(255,255,255,.25); }
    .loop-btn.active { background: rgba(255,255,255,.92); color: #4f7cff; border-color: transparent; }

    /* Article */
    .article-body { font-size: 1.05rem; line-height: 1.9; }
    .article-body p { margin-bottom: 1.1rem; }
    .article-body p:last-child { margin-bottom: 0; }
    .vocab-word { background: var(--highlight); border-bottom: 2px solid var(--accent2); padding: 0 2px; border-radius: 2px; font-weight: 700; cursor: pointer; transition: background .15s; }
    .vocab-word:hover { background: #fef3c7; }
    .phrase-chunk { background: var(--phrase-bg); border-bottom: 2px solid var(--phrase-border); padding: 0 2px; border-radius: 2px; cursor: pointer; transition: background .15s; }
    .phrase-chunk:hover { background: #dcfce7; }
    .review-word { background: #f3e8ff; border-bottom: 2px solid #a855f7; padding: 0 2px; border-radius: 2px; font-weight: 700; cursor: pointer; transition: background .15s; }
    .review-word:hover { background: #ede9fe; }

    /* Sentence playback */
    .sent { display: inline; }
    .sent-btn { display: inline-flex; align-items: center; justify-content: center; width: 18px; height: 18px; border-radius: 50%; background: none; border: 1.5px solid #c7d2fe; color: var(--accent); cursor: pointer; font-size: .55rem; vertical-align: middle; margin: 0 3px 0 0; flex-shrink: 0; transition: all .15s; padding: 0; line-height: 1; }
    .sent-btn:hover { border-color: var(--accent); background: var(--tag-bg); }
    .sent-btn.playing { background: var(--accent); border-color: var(--accent); color: white; }

    /* Popup */
    #word-popup { position: fixed; z-index: 9999; max-width: 300px; min-width: 220px; background: white; border-radius: 16px; box-shadow: 0 8px 32px rgba(0,0,0,.18); padding: 1.1rem 1.2rem 1rem; display: none; font-family: sans-serif; animation: popIn .15s ease; border: 1px solid var(--border); }
    @keyframes popIn { from { opacity:0; transform:translateY(6px) scale(.97); } to { opacity:1; transform:translateY(0) scale(1); } }
    #word-popup .pop-word { font-size: 1.1rem; font-weight: 700; margin-bottom: .25rem; display: flex; align-items: center; gap: .5rem; flex-wrap: wrap; }
    #word-popup .pop-badge { font-size: .7rem; font-weight: 700; padding: .15rem .5rem; border-radius: 4px; background: var(--tag-bg); color: var(--tag-text); white-space: nowrap; }
    #word-popup .pop-badge.vocab { background: #fffbeb; color: #92400e; }
    #word-popup .pop-badge.phrase { background: #f0fdf4; color: #166534; }
    #word-popup .pop-badge.review { background: #f3e8ff; color: #7e22ce; }
    #word-popup .pop-note { font-size: .82rem; color: var(--muted); line-height: 1.5; margin-top: .2rem; }
    #word-popup .pop-def { font-size: .85rem; color: var(--muted); line-height: 1.5; margin-top: .2rem; }
    #word-popup .pop-example { font-size: .82rem; color: var(--muted); font-style: italic; margin-top: .4rem; padding-top: .4rem; border-top: 1px solid var(--border); line-height: 1.5; }
    #word-popup .pop-loading { font-size: .85rem; color: var(--muted); display: flex; align-items: center; gap: .4rem; margin-top: .3rem; }
    #word-popup .pop-loading::before { content:''; width:12px; height:12px; border:2px solid var(--border); border-top-color:var(--accent); border-radius:50%; animation:spin .6s linear infinite; flex-shrink:0; }
    @keyframes spin { to { transform:rotate(360deg); } }
    #word-popup .pop-close { position:absolute; top:.5rem; right:.6rem; width:20px; height:20px; background:#f3f4f6; border:none; border-radius:50%; cursor:pointer; font-size:.7rem; color:var(--muted); display:flex; align-items:center; justify-content:center; }
    #word-popup .pop-close:hover { background:var(--border); }
    #word-popup .pop-type-badge { display:inline-block; font-size:.7rem; font-weight:700; padding:.15rem .5rem; border-radius:4px; background:#eff6ff; color:#1d4ed8; margin:.2rem 0 .35rem; }
    #word-popup .pop-zh-btn { margin-top:.6rem; padding:.35rem .85rem; background:var(--tag-bg); color:var(--accent); border:1.5px solid var(--accent); border-radius:8px; font-size:.82rem; font-weight:600; cursor:pointer; font-family:sans-serif; transition:all .15s; display:block; width:100%; text-align:center; }
    #word-popup .pop-zh-btn:hover { background:var(--accent); color:white; }
    #word-popup .pop-zh { font-size:.95rem; font-weight:700; margin-top:.5rem; color:#166534; padding:.4rem .6rem; background:#f0fdf4; border-radius:6px; }

    /* Review tags */
    .review-tag { display:inline-block; font-size:.7rem; font-weight:700; padding:.15rem .5rem; border-radius:99px; white-space:nowrap; }
    .review-tag.today { background:#fef3c7; color:#92400e; }
    .review-tag.overdue { background:#fef2f2; color:#991b1b; }
    .review-tag.upcoming { background:#f0fdf4; color:#166534; }

    /* Vocab table */
    .vocab-table { width: 100%; border-collapse: collapse; font-family: sans-serif; font-size: .88rem; }
    .vocab-table thead tr { background: var(--tag-bg); }
    .vocab-table th { text-align: left; padding: .6rem .9rem; font-weight: 700; color: var(--tag-text); font-size: .75rem; letter-spacing: .05em; text-transform: uppercase; }
    .vocab-table td { padding: .7rem .9rem; border-bottom: 1px solid var(--border); vertical-align: top; line-height: 1.5; }
    .vocab-table tr:last-child td { border-bottom: none; }
    .vocab-table tr:hover td { background: #fafafa; }
    .pos-badge { display:inline-block; background:#f3f4f6; color:var(--muted); font-size:.72rem; padding:.15rem .5rem; border-radius:4px; font-weight:600; }
    .zh-meaning { font-weight: 600; }
    .example-sent { color: var(--muted); font-style: italic; margin-top: .15rem; font-size: .83rem; }

    /* Phrase list */
    .phrase-list { display: flex; flex-direction: column; gap: .85rem; }
    .phrase-item { padding: .8rem 1rem; background: var(--phrase-bg); border-left: 3px solid var(--phrase-border); border-radius: 0 10px 10px 0; }
    .phrase-item .ph-text { font-weight: 700; font-size: .95rem; font-family: sans-serif; }
    .phrase-item .ph-zh { font-size: .88rem; color: #166534; margin-top: .2rem; }
    .phrase-item .ph-note { font-size: .82rem; color: var(--muted); margin-top: .25rem; font-style: italic; }

    /* Quiz */
    .quiz-q { margin-bottom: 1.6rem; }
    .quiz-q:last-child { margin-bottom: 0; }
    .quiz-question { font-size: 1rem; font-weight: 600; margin-bottom: .75rem; line-height: 1.5; }
    .quiz-options { display: flex; flex-direction: column; gap: .45rem; }
    .quiz-option { display: flex; align-items: center; gap: .7rem; padding: .65rem 1rem; border: 1.5px solid var(--border); border-radius: 10px; cursor: pointer; font-family: sans-serif; font-size: .9rem; transition: all .15s; background: white; }
    .quiz-option:hover { border-color: var(--accent); background: var(--tag-bg); }
    .quiz-option.correct { border-color: var(--green); background: #f0fdf4; color: #166534; font-weight: 600; }
    .quiz-option.wrong { border-color: var(--red); background: #fef2f2; color: #991b1b; }
    .opt-key { width:24px; height:24px; border-radius:6px; background:var(--tag-bg); color:var(--accent); font-weight:700; font-size:.8rem; display:flex; align-items:center; justify-content:center; flex-shrink:0; transition:all .15s; }
    .quiz-option.correct .opt-key { background: var(--green); color: white; }
    .quiz-option.wrong .opt-key { background: var(--red); color: white; }
    .answers-btn { margin-top: 1.2rem; padding: .65rem 1.4rem; background: var(--accent); color: white; border: none; border-radius: 10px; font-family: sans-serif; font-size: .88rem; font-weight: 600; cursor: pointer; }
    .answers-btn:hover { background: #3a66e0; }
    .answers-reveal { display: none; margin-top: 1rem; padding: .9rem 1.1rem; background: #f0fdf4; border: 1.5px solid #bbf7d0; border-radius: 10px; font-family: sans-serif; font-size: .9rem; color: #166534; font-weight: 600; }

    /* Tips */
    .tips-box { background: var(--highlight); border-left: 4px solid var(--accent2); border-radius: 0 12px 12px 0; padding: 1rem 1.2rem; font-family: sans-serif; font-size: .92rem; line-height: 1.7; color: #78350f; }

    /* Review */
    .review-msg { font-family: sans-serif; font-size: .95rem; color: var(--muted); text-align: center; padding: 1rem 0; }

    /* Legend */
    .legend { display: flex; gap: 1rem; font-family: sans-serif; font-size: .8rem; color: var(--muted); margin-bottom: 1rem; flex-wrap: wrap; }
    .legend-item { display: flex; align-items: center; gap: .35rem; }
    .legend-dot { width: 10px; height: 10px; border-radius: 2px; }
    .legend-dot.vocab { background: #fef3c7; border-bottom: 2px solid var(--accent2); }
    .legend-dot.review { background: #f3e8ff; border-bottom: 2px solid #a855f7; }
    .legend-dot.phrase { background: var(--phrase-bg); border-bottom: 2px solid var(--phrase-border); }
    .sentence-mode { display: inline-flex; align-items: center; gap: .45rem; }
    .sentence-mode-label { color: var(--accent); font-weight: 700; }
    .sentence-mode-group { display: inline-flex; align-items: center; gap: .2rem; padding: .2rem; background: var(--tag-bg); border-radius: 99px; }
    .sentence-mode-btn { border: none; background: transparent; color: var(--accent); border-radius: 99px; padding: .28rem .72rem; font-family: sans-serif; font-size: .76rem; font-weight: 700; cursor: pointer; transition: all .15s; }
    .sentence-mode-btn:hover { background: rgba(79,124,255,.12); }
    .sentence-mode-btn.active { background: var(--accent); color: white; }

    /* Active Recall Quiz */
    .rq-subtitle { font-family: sans-serif; font-size: .88rem; color: var(--muted); margin-bottom: 1.3rem; }
    .rq-item { margin-bottom: 1.5rem; padding-bottom: 1.5rem; border-bottom: 1px solid var(--border); }
    .rq-item:last-of-type { border-bottom: none; padding-bottom: 0; margin-bottom: 0; }
    .rq-zh { font-size: 1rem; font-weight: 700; margin-bottom: .6rem; }
    .rq-pos { font-size: .75rem; font-weight: 400; color: var(--muted); font-family: sans-serif; margin-left: .3rem; }
    .rq-hint { font-size: .85rem; color: var(--muted); font-style: italic; margin-bottom: .6rem; line-height: 1.5; }
    .rq-opts { display: grid; grid-template-columns: 1fr 1fr; gap: .45rem; }
    .rq-opt { padding: .6rem .8rem; border: 1.5px solid var(--border); border-radius: 10px; background: white; cursor: pointer; font-family: 'Georgia', serif; font-size: .88rem; transition: all .15s; text-align: left; }
    .rq-opt:hover:not([disabled]) { border-color: var(--accent); background: var(--tag-bg); }
    .rq-opt.selected { border-color: var(--accent); background: var(--tag-bg); font-weight: 700; }
    .rq-opt.correct { border-color: var(--green); background: #f0fdf4; color: #166534; font-weight: 700; }
    .rq-opt.wrong { border-color: var(--red); background: #fef2f2; color: #991b1b; font-weight: 700; }
    #rq-submit-btn { margin-top: 1.4rem; padding: .75rem 1.4rem; background: var(--accent); color: white; border: none; border-radius: 10px; font-family: sans-serif; font-size: .92rem; font-weight: 700; cursor: pointer; width: 100%; transition: background .15s; }
    #rq-submit-btn:hover:not([disabled]) { background: #3a66e0; }
    #rq-submit-btn:disabled { background: var(--muted); cursor: default; }
    #rq-result { margin-top: 1rem; padding: 1rem 1.2rem; border-radius: 10px; font-family: sans-serif; font-size: .9rem; line-height: 1.7; }
    #rq-result.success { background: #f0fdf4; border: 1.5px solid #bbf7d0; color: #166534; }
    #rq-result.partial { background: #fffbeb; border: 1.5px solid #fde68a; color: #92400e; }

    /* Speaking Bridge */
    .bridge-subtitle { font-family: sans-serif; font-size: .88rem; color: var(--muted); margin-bottom: 1.3rem; line-height: 1.6; }
    .bridge-item { border: 1.5px solid var(--border); border-radius: 14px; padding: 1.2rem 1.3rem; margin-bottom: 1.1rem; }
    .bridge-item:last-child { margin-bottom: 0; }
    .bridge-word-header { display: flex; align-items: center; gap: .5rem; margin-bottom: 1rem; flex-wrap: wrap; }
    .bridge-word { font-size: 1.05rem; font-weight: 700; font-family: 'Georgia', serif; }
    .bridge-word-zh { font-size: 1.05rem; font-weight: 700; font-family: sans-serif; color: #166534; }
    .bridge-day-badge { margin-left: auto; font-family: sans-serif; font-size: .72rem; font-weight: 700; padding: .15rem .55rem; border-radius: 99px; background: #fef3c7; color: #92400e; }
    .bridge-level { margin-bottom: .85rem; padding-bottom: .85rem; border-bottom: 1px dashed var(--border); }
    .bridge-level:last-child { margin-bottom: 0; padding-bottom: 0; border-bottom: none; }
    .bridge-level-label { font-family: sans-serif; font-size: .7rem; font-weight: 700; color: var(--accent); letter-spacing: .06em; text-transform: uppercase; margin-bottom: .45rem; }
    .bridge-sentence { font-size: .95rem; line-height: 1.75; margin-bottom: .5rem; }
    .bridge-blank { font-weight: 700; color: #9ca3af; letter-spacing: .12em; }
    .bridge-zh-prompt { font-family: sans-serif; font-size: .9rem; color: #166534; background: #f0fdf4; padding: .4rem .75rem; border-radius: 8px; margin-bottom: .5rem; line-height: 1.65; }
    .bridge-scramble { font-family: sans-serif; font-size: .86rem; color: var(--muted); background: #f3f4f6; padding: .45rem .8rem; border-radius: 8px; margin-bottom: .5rem; line-height: 1.85; word-break: break-word; }
    .bridge-reveal-btn { padding: .38rem 1rem; border: 1.5px solid var(--accent); color: var(--accent); background: white; border-radius: 8px; font-family: sans-serif; font-size: .82rem; font-weight: 600; cursor: pointer; transition: all .15s; }
    .bridge-reveal-btn:hover { background: var(--accent); color: white; }
    .bridge-answer { margin-top: .5rem; padding: .5rem .85rem; background: var(--tag-bg); border-radius: 8px; font-size: .9rem; font-weight: 600; color: var(--accent); font-family: sans-serif; line-height: 1.6; }
    .bridge-none { font-family: sans-serif; font-size: .92rem; color: var(--muted); text-align: center; padding: .8rem 0; }

    @media (max-width: 500px) {
      .card { padding: 1.4rem 1.2rem; }
      .player-card { padding: 1.3rem 1.2rem; }
      .header h1 { font-size: 1.3rem; }
      .rq-opts { grid-template-columns: 1fr; }
    }
  </style>
</head>
<body>
<div class="container">

  <div class="header">
    <div class="date-badge">[英文月份 日, 年] · Day [累計天數]</div>
    <h1>[文章標題，關鍵詞用 <span> 包住]</h1>
    <p class="subtitle">A2 → B1 · Daily English Reading</p>
  </div>

  <div class="player-card">
    <div class="player-label">🎧 Listen to the Article</div>
    <div class="player-title">[文章標題]</div>
    <audio id="article-audio" controls>
      <source src="article.mp3" type="audio/mpeg" />
    </audio>
    <div class="player-controls">
      <button class="loop-btn" onclick="toggleLoop(this)">🔁 循環播放</button>
    </div>
  </div>

  <div id="word-popup">
    <button class="pop-close" onclick="closePopup()">✕</button>
    <div id="pop-content"></div>
  </div>

  <div class="card">
    <div class="card-title">📖 Today's Article</div>
    <div class="legend">
      <div class="legend-item"><div class="legend-dot vocab"></div>今日單字</div>
      <div class="legend-item"><div class="legend-dot review"></div>複習單字</div>
      <div class="legend-item"><div class="legend-dot phrase"></div>重要片語</div>
      <div class="legend-item" style="color:var(--accent);font-size:.8rem;">🔊 點擊播放單句</div>
      <div class="legend-item sentence-mode">
        <span class="sentence-mode-label">單句模式</span>
        <span class="sentence-mode-group" role="group" aria-label="單句播放模式">
          <button type="button" class="sentence-mode-btn active" data-mode="once" onclick="setSentenceMode('once', this)">單次</button>
          <button type="button" class="sentence-mode-btn" data-mode="loop" onclick="setSentenceMode('loop', this)">循環</button>
        </span>
      </div>
    </div>
    <div class="article-body" id="article-body">
      <!--
        每個句子用 <span class="sent" data-idx="N" data-text="純文字句子（不含 HTML）"> 包住。
        句子內的單字和片語仍用 vocab-word / phrase-chunk span。
        每句開頭放一個播放按鈕：<button class="sent-btn" onclick="playSent(this)" title="播放這句">🔊</button>

        範例格式（兩段、三句）：
        <p>
          <span class="sent" data-idx="1" data-text="I went to the market."><button class="sent-btn" onclick="playSent(this)" title="播放這句">🔊</button>I went to the <span class="vocab-word" data-word="market">market</span>.</span>
          <span class="sent" data-idx="2" data-text="It was very busy and I felt exhausted."><button class="sent-btn" onclick="playSent(this)" title="播放這句">🔊</button>It was very busy and I felt <span class="review-word" data-word="exhausted">exhausted</span>.</span>
        </p>
        <p>
          <span class="sent" data-idx="3" data-text="I picked up some fresh vegetables."><button class="sent-btn" onclick="playSent(this)" title="播放這句">🔊</button>I <span class="phrase-chunk" data-phrase="picked up">picked up</span> some fresh vegetables.</span>
        </p>

        標記規則：
        - 今日新單字：vocab-word（橘色）
        - 融入文章的複習單字：review-word（紫色）
        - 重要片語：phrase-chunk（綠色）
        - data-idx 從 1 開始連續編號（跨段落不重設）
        - data-text 必須是純文字，不含任何 HTML tag
      -->
      [文章段落 HTML]
    </div>
  </div>

  <div class="card">
    <div class="card-title">📚 New Words Today</div>
    <table class="vocab-table">
      <thead><tr><th>Word</th><th>詞性</th><th>中文 / Example</th></tr></thead>
      <tbody>
        <!-- 每個單字一行：
        <tr>
          <td><strong>word</strong></td>
          <td><span class="pos-badge">n.</span></td>
          <td><div class="zh-meaning">中文意思</div><div class="example-sent">Example sentence.</div></td>
        </tr>
        -->
        [單字表 HTML]
      </tbody>
    </table>
  </div>

  <div class="card">
    <div class="card-title">🔗 Key Phrases</div>
    <div class="phrase-list">
      <!-- 每個片語：
      <div class="phrase-item">
        <div class="ph-text">go through</div>
        <div class="ph-zh">通過、經歷（某個過程）</div>
        <div class="ph-note">文章用法：go through security → 通過安檢</div>
      </div>
      -->
      [片語列表 HTML]
    </div>
  </div>

  <div class="card">
    <div class="card-title">✏️ Quiz</div>
    <!-- 3 題測驗，正確答案的 quiz-option 用 onclick="answer(this,'correct')"，錯誤用 onclick="answer(this,'wrong')" -->
    [測驗 HTML]
    <button class="answers-btn" onclick="toggleAnswers()">顯示答案</button>
    <div class="answers-reveal" id="answers-reveal">
      ✅ &nbsp;Q1: <strong>[答案]</strong> &nbsp;｜&nbsp; Q2: <strong>[答案]</strong> &nbsp;｜&nbsp; Q3: <strong>[答案]</strong>
    </div>
  </div>

  <div class="card">
    <div class="card-title">🧠 Active Recall Quiz</div>
    <p class="rq-subtitle">看中文意思，選出正確的英文單字</p>
    <!--
      填寫說明：
      若有到期複習單字，為每個出一題（格式如下）：
      <div class="rq-item" data-word="[英文單字原文]" data-correct="[正確答案值，與某個選項的 data-val 完全一致]">
        <div class="rq-zh">[中文意思] <span class="rq-pos">[詞性]</span></div>
        <div class="rq-opts">
          <button class="rq-opt" data-val="[選項A]" onclick="rqSelect(this)">[選項A]</button>
          <button class="rq-opt" data-val="[選項B]" onclick="rqSelect(this)">[選項B]</button>
          <button class="rq-opt" data-val="[選項C]" onclick="rqSelect(this)">[選項C]</button>
          <button class="rq-opt" data-val="[選項D]" onclick="rqSelect(this)">[選項D]</button>
        </div>
      </div>
      注意：4 個選項中 1 個正確 + 3 個干擾，隨機順序排列，正確答案不可固定在同一位置。
      若今天無到期複習單字：
      <div class="review-msg">今天沒有需要複習的單字！繼續保持 💪</div>
    -->
    [REVIEW_QUIZ_HTML]
    <div id="rq-result" style="display:none"></div>
    <button id="rq-submit-btn" onclick="submitReviewQuiz()">提交答案 &amp; 保存 SRS 記錄</button>
    <div id="repo-target-hint" class="review-msg" style="padding:.7rem 0 .1rem; font-size:.86rem;"></div>
    <button id="repo-target-edit-btn" class="answers-btn" style="margin-top:.6rem;" onclick="editRepoTarget()">修改同步目標倉庫</button>
    <button id="local-export-btn" class="answers-btn" style="margin-top:.6rem; display:none;" onclick="exportLocalLearningJson()">匯出本地 learning.json</button>
    <button id="local-import-btn" class="answers-btn" style="margin-top:.6rem; display:none;" onclick="importLocalLearningJson()">匯入本地 learning.json</button>
    <input id="local-import-input" type="file" accept="application/json,.json" style="display:none" onchange="handleLocalLearningImport(event)" />
    <div id="local-store-info" class="review-msg" style="padding:.6rem 0 0; font-size:.84rem; display:none;"></div>
  </div>

  <div class="card">
    <div class="card-title">🌉 Speaking Bridge</div>
    <p class="bridge-subtitle">用 2–7 天前學的單字練習開口<br>短期記憶已淡，這才是真正的記憶測試 💪</p>
    <!--
      橋接訓練說明：
      從 learning.json 取 dateAdded 在 2–7 天前的單字（最多 4 個）。
      每個單字出 3 層練習，全部用 bridgeReveal(btn) 翻牌顯示答案。

      有單字時，每個單字格式如下：
      <div class="bridge-item">
        <div class="bridge-word-header">
          <span class="bridge-word-zh">日常慣例</span>
          <span class="pos-badge">n.</span>
          <span class="bridge-day-badge">3 天前</span>
        </div>
        <div class="bridge-level">
          <div class="bridge-level-label">Lv.1 重組＋填空</div>
          <div class="bridge-zh-prompt">「[該句的中文翻譯]」</div>
          <div class="bridge-scramble">keep / morning / to / I / a / try / <span class="bridge-blank">____</span> / healthy</div>
          <button class="bridge-reveal-btn" onclick="bridgeReveal(this)">顯示答案</button>
          <div class="bridge-answer" style="display:none">I try to keep a healthy morning routine.</div>
        </div>
        <div class="bridge-level">
          <div class="bridge-level-label">Lv.2 中翻英（新情境）</div>
          <div class="bridge-zh-prompt">「你有固定的睡前習慣嗎？」先試著說出英文，再點顯示。</div>
          <button class="bridge-reveal-btn" onclick="bridgeReveal(this)">顯示參考答案</button>
          <div class="bridge-answer" style="display:none">Do you have a bedtime routine?</div>
        </div>
      </div>

      學習天數不足時（2–7天前無單字）：
      <div class="bridge-none">學習天數尚不足 2 天，明天開始會出現橋接練習！加油 💪</div>
    -->
    [BRIDGE_HTML]
  </div>

  <div class="card">
    <div class="card-title">💡 Learning Tips</div>
    <div class="tips-box">[今日學習建議，繁體中文]</div>
  </div>

  <div class="card">
    <div class="card-title">🔁 Review Words</div>
    <!--
    有到期複習單字時，每個單字顯示一行，加上狀態標籤：
    <table class="vocab-table">
      <thead><tr><th>Word</th><th>詞性</th><th>中文 / Example</th><th>狀態</th></tr></thead>
      <tbody>
        <tr>
          <td><strong>example</strong></td>
          <td><span class="pos-badge">n.</span></td>
          <td><div class="zh-meaning">例子</div><div class="example-sent">This is an example.</div></td>
          <td><span class="review-tag today">今天複習 🔔</span></td>
        </tr>
        <tr>
          <td><strong>airport</strong></td>
          <td><span class="pos-badge">n.</span></td>
          <td><div class="zh-meaning">機場</div><div class="example-sent">We arrived at the airport early.</div></td>
          <td><span class="review-tag overdue">逾期 2 天 ⚠️</span></td>
        </tr>
      </tbody>
    </table>

    無到期單字但有未來複習時：
    <div class="review-msg">今天沒有到期的複習 ✅ 下一個複習：<strong>stressful</strong>（還有 2 天）</div>

    完全沒有任何單字（第一天）：
    <div class="review-msg">今天是第一天，明天開始會有複習單字！加油 💪</div>
    -->
    [複習單字 HTML]
  </div>

</div>
<script src="https://cdn.jsdelivr.net/npm/opencc-js@1.4.0/dist/umd/full.js"></script>
<script>
  function getAssetBasePath() {
    const path = window.location.pathname;
    if (path.endsWith('/')) return path;
    if (/\.[^/]+$/.test(path)) return path.replace(/[^/]+$/, '');
    return path + '/';
  }

  function buildAssetUrl(filename) {
    return getAssetBasePath() + filename;
  }

  const REVIEW_SYNC_MODE = localStorage.getItem('review_sync_mode') || 'local';
  const LOCAL_LEARNING_KEY = 'learning_json_local';
  const ZH_SCRIPT_MODE = localStorage.getItem('zh_script_mode') || 'simplified';
  let zhConverter = null;

  function ensureZhConverter() {
    if (zhConverter) return zhConverter;
    if (window.OpenCC && typeof window.OpenCC.Converter === 'function') {
      zhConverter = window.OpenCC.Converter({ from: 'tw', to: 'cn' });
    }
    return zhConverter;
  }

  function toSimplifiedText(text) {
    if (typeof text !== 'string' || ZH_SCRIPT_MODE !== 'simplified') return text;
    const converter = ensureZhConverter();
    return converter ? converter(text) : text;
  }

  function convertElementToSimplified(root) {
    if (ZH_SCRIPT_MODE !== 'simplified') return;
    const converter = ensureZhConverter();
    if (!converter || !root) return;

    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
    const nodes = [];
    let node;
    while ((node = walker.nextNode())) {
      const parent = node.parentElement;
      if (!parent) continue;
      if (['SCRIPT', 'STYLE'].includes(parent.tagName)) continue;
      if (/[\u4e00-\u9fff]/.test(node.nodeValue || '')) nodes.push(node);
    }
    nodes.forEach(n => {
      n.nodeValue = converter(n.nodeValue);
    });

    if (root.querySelectorAll) {
      root.querySelectorAll('[title], [placeholder], [aria-label]').forEach(el => {
        ['title', 'placeholder', 'aria-label'].forEach(attr => {
          const val = el.getAttribute(attr);
          if (val && /[\u4e00-\u9fff]/.test(val)) {
            el.setAttribute(attr, converter(val));
          }
        });
      });
    }
  }

  function applySimplifiedChinese() {
    if (ZH_SCRIPT_MODE !== 'simplified') return;
    convertElementToSimplified(document.body);
    document.title = toSimplifiedText(document.title);
  }

  function getLearningJsonUrl() {
    return new URL('../../vocabulary/learning.json', window.location.href).href;
  }

  async function loadLocalLearningJson() {
    const cached = localStorage.getItem(LOCAL_LEARNING_KEY);
    if (cached) return JSON.parse(cached);
    const resp = await fetch(getLearningJsonUrl(), { cache: 'no-store' });
    if (!resp.ok) throw new Error('讀取本地 learning.json 失敗 (' + resp.status + ')');
    const json = await resp.json();
    localStorage.setItem(LOCAL_LEARNING_KEY, JSON.stringify(json));
    return json;
  }

  function saveLocalLearningJson(vocab) {
    localStorage.setItem(LOCAL_LEARNING_KEY, JSON.stringify(vocab));
  }

  async function refreshLocalStoreInfo() {
    const el = document.getElementById('local-store-info');
    if (!el) return;
    if (REVIEW_SYNC_MODE !== 'local') {
      el.style.display = 'none';
      return;
    }
    try {
      const vocab = await loadLocalLearningJson();
      const count = Array.isArray(vocab.words) ? vocab.words.length : 0;
      el.textContent = '本機 learning.json：' + count + ' 個單字';
      el.style.display = 'block';
    } catch (err) {
      el.textContent = '本機 learning.json 讀取失敗：' + err.message;
      el.style.display = 'block';
    }
  }

  function exportLocalLearningJson() {
    const raw = localStorage.getItem(LOCAL_LEARNING_KEY);
    if (!raw) {
      alert('目前沒有可匯出的本地 learning.json');
      return;
    }
    const blob = new Blob([raw], { type: 'application/json;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'learning.local.json';
    document.body.appendChild(a);
    a.click();
    a.remove();
    URL.revokeObjectURL(url);
  }

  function importLocalLearningJson() {
    const input = document.getElementById('local-import-input');
    if (!input) return;
    input.value = '';
    input.click();
  }

  function handleLocalLearningImport(event) {
    const file = event.target.files && event.target.files[0];
    if (!file) return;
    const reader = new FileReader();
    reader.onload = () => {
      try {
        const parsed = JSON.parse(String(reader.result || ''));
        if (!parsed || !Array.isArray(parsed.words)) {
          throw new Error('格式錯誤：需要包含 words 陣列');
        }
        localStorage.setItem(LOCAL_LEARNING_KEY, JSON.stringify(parsed));
        refreshLocalStoreInfo();
        alert('已匯入本地 learning.json（' + parsed.words.length + ' 個單字）');
      } catch (err) {
        alert('匯入失敗：' + err.message);
      }
    };
    reader.onerror = () => {
      alert('匯入失敗：檔案讀取錯誤');
    };
    reader.readAsText(file, 'utf-8');
  }

  // Sentence-by-sentence playback
  const sentAudio = new Audio();
  let activeSentBtn = null;
  let sentencePlaybackMode = 'once';

  function resetSentBtn(btn) {
    if (!btn) return;
    btn.classList.remove('playing');
    btn.textContent = '🔊';
  }

  function stopSentencePlayback() {
    sentAudio.pause();
    sentAudio.currentTime = 0;
    sentAudio.loop = false;
    resetSentBtn(activeSentBtn);
    activeSentBtn = null;
  }

  function syncSentenceModeButtons() {
    document.querySelectorAll('.sentence-mode-btn').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.mode === sentencePlaybackMode);
    });
  }

  function setSentenceMode(mode) {
    sentencePlaybackMode = mode;
    syncSentenceModeButtons();
    if (activeSentBtn && !sentAudio.paused) {
      sentAudio.loop = sentencePlaybackMode === 'loop';
    }
  }

  function playSent(btn) {
    const idx = btn.closest('.sent').dataset.idx;
    const src = buildAssetUrl(`s${String(idx).padStart(2,'0')}.mp3`);
    if (activeSentBtn === btn && !sentAudio.paused) {
      stopSentencePlayback();
      return;
    }
    stopSentencePlayback();
    sentAudio.src = src;
    sentAudio.loop = sentencePlaybackMode === 'loop';
    activeSentBtn = btn; btn.classList.add('playing'); btn.textContent = '⏸';
    sentAudio.onended = () => {
      if (sentAudio.loop) return;
      resetSentBtn(btn);
      activeSentBtn = null;
    };
    sentAudio.onerror = () => {
      stopSentencePlayback();
    };
    sentAudio.play();
  }

  // Quiz
  function answer(el, type) {
    const group = el.closest('.quiz-options');
    if (group.querySelector('.correct, .wrong')) return;
    el.classList.add(type);
  }
  function toggleAnswers() {
    const el = document.getElementById('answers-reveal');
    const btn = document.querySelector('.answers-btn');
    if (el.style.display === 'block') { el.style.display='none'; btn.textContent='顯示答案'; }
    else { el.style.display='block'; btn.textContent='隱藏答案'; }
  }

  // Active Recall Quiz
  function rqSelect(btn) {
    const opts = btn.closest('.rq-opts').querySelectorAll('.rq-opt');
    opts.forEach(b => b.classList.remove('selected'));
    btn.classList.add('selected');
  }

  function getRepoTarget() {
    const owner = localStorage.getItem('github_repo_owner') || 'CarryJone';
    const repo = localStorage.getItem('github_repo_name') || 'english-learning';
    return { owner, repo };
  }

  function refreshRepoTargetHint() {
    const el = document.getElementById('repo-target-hint');
    if (!el) return;
    const target = getRepoTarget();
    el.textContent = '目前同步目標：' + target.owner + '/' + target.repo;
  }

  function editRepoTarget() {
    const current = getRepoTarget();
    const ownerInput = prompt('GitHub repo owner（你的帳號）', current.owner);
    if (!ownerInput) return;
    const repoInput = prompt('GitHub repo name', current.repo);
    if (!repoInput) return;
    localStorage.setItem('github_repo_owner', ownerInput.trim());
    localStorage.setItem('github_repo_name', repoInput.trim());
    refreshRepoTargetHint();
  }

  async function submitReviewQuiz() {
    const items = document.querySelectorAll('.rq-item');
    if (!items.length) return;

    // Collect answers
    const results = [];
    let allAnswered = true;
    items.forEach(item => {
      const sel = item.querySelector('.rq-opt.selected');
      if (!sel) { allAnswered = false; return; }
      results.push({ word: item.dataset.word, correct: sel.dataset.val === item.dataset.correct });
    });
    if (!allAnswered) { alert('請先回答所有題目！'); return; }

    const selectedByWord = {};
    items.forEach(item => {
      const sel = item.querySelector('.rq-opt.selected');
      if (sel) selectedByWord[item.dataset.word] = sel.dataset.val;
    });

    // Show correct/wrong on each question
    items.forEach(item => {
      const correct = item.dataset.correct;
      item.querySelectorAll('.rq-opt').forEach(b => {
        b.setAttribute('disabled', '');
        if (b.dataset.val === correct) b.classList.add('correct');
        else if (b.classList.contains('selected')) b.classList.add('wrong');
        b.classList.remove('selected');
      });
    });

    const today = new Date().toISOString().slice(0, 10);
    const storageKey = 'rq_done_' + today;
    const score = results.filter(r => r.correct).length;
    const submitBtn = document.getElementById('rq-submit-btn');
    const resultEl = document.getElementById('rq-result');

    // Extra practice protection: already submitted today
    if (localStorage.getItem(storageKey)) {
      resultEl.innerHTML = '✅ 今天已完成複習（額外練習）：' + score + '/' + results.length + ' 題答對，SRS 未更新';
      convertElementToSimplified(resultEl);
      resultEl.className = 'success';
      resultEl.style.display = 'block';
      submitBtn.textContent = '已完成'; submitBtn.disabled = true;
      return;
    }

    submitBtn.disabled = true; submitBtn.textContent = '處理中...';

    if (REVIEW_SYNC_MODE === 'local') {
      try {
        const vocab = await loadLocalLearningJson();
        const SRS = [1, 3, 7, 14, 30, 60, 90];
        for (const r of results) {
          const w = vocab.words.find(x => x.word === r.word);
          if (!w || w.lastReviewedDate === today) continue;
          w.lastReviewedDate = today;
          const next = new Date();
          if (r.correct) {
            w.reviewCount = (w.reviewCount || 0) + 1;
            next.setDate(next.getDate() + (SRS[Math.min(w.reviewCount, SRS.length - 1)] || 90));
          } else {
            w.reviewCount = 0;
            next.setDate(next.getDate() + 1);
          }
          w.nextReview = next.toISOString().slice(0, 10);
        }
        saveLocalLearningJson(vocab);
        await refreshLocalStoreInfo();
        localStorage.setItem(storageKey, '1');
        resultEl.innerHTML = '🎉 複習完成！' + score + '/' + results.length + ' 題答對，已保存到本機（localStorage） ✅';
        convertElementToSimplified(resultEl);
        resultEl.className = (score === results.length) ? 'success' : 'partial';
        resultEl.style.display = 'block';
        submitBtn.textContent = '✅ 已保存（本機）';
        return;
      } catch (err) {
        items.forEach(item => {
          const prev = selectedByWord[item.dataset.word];
          item.querySelectorAll('.rq-opt').forEach(b => {
            b.removeAttribute('disabled');
            b.classList.remove('correct', 'wrong', 'selected');
            if (prev && b.dataset.val === prev) b.classList.add('selected');
          });
        });
        submitBtn.disabled = false;
        submitBtn.textContent = '提交答案 & 保存 SRS 記錄';
        alert('本地保存失敗：' + err.message);
        return;
      }
    }

    try {
      const readGitHubError = async (resp) => {
        try {
          const data = await resp.json();
          if (!data || !data.message) return '';
          if (!Array.isArray(data.errors) || !data.errors.length) return ' - ' + data.message;
          const parts = data.errors.map(e => e && (e.message || e.code || JSON.stringify(e))).filter(Boolean);
          return ' - ' + data.message + (parts.length ? ' | ' + parts.join('; ') : '');
        } catch (_) {
          return '';
        }
      };

      // Get GitHub PAT from localStorage (reprompt on auth failure)
      const askToken = () => {
        const t = prompt('請輸入 GitHub Personal Access Token（repo write 權限，儲存在本機）：');
        if (!t) throw new Error('未提供 Token，無法同步');
        const trimmed = t.trim();
        localStorage.setItem('github_pat', trimmed);
        return trimmed;
      };

      let token = localStorage.getItem('github_pat');
      if (!token) token = askToken();

      const askRepoConfig = () => {
        const current = getRepoTarget();
        const ownerInput = prompt('GitHub repo owner（你的帳號）', current.owner);
        if (!ownerInput) throw new Error('未提供 repo owner，無法同步');
        const repoInput = prompt('GitHub repo name', current.repo);
        if (!repoInput) throw new Error('未提供 repo name，無法同步');
        const owner = ownerInput.trim();
        const repo = repoInput.trim();
        localStorage.setItem('github_repo_owner', owner);
        localStorage.setItem('github_repo_name', repo);
        refreshRepoTargetHint();
        return { owner, repo };
      };

      let owner = localStorage.getItem('github_repo_owner') || 'CarryJone';
      let repo = localStorage.getItem('github_repo_name') || 'english-learning';
      const filePath = 'vocabulary/learning.json';
      let apiBase = 'https://api.github.com/repos/' + owner + '/' + repo + '/contents/' + filePath;

      // Read current learning.json
      let getResp = await fetch(apiBase, {
        headers: { Authorization: 'token ' + token, Accept: 'application/vnd.github.v3+json' }
      });
      if (getResp.status === 401 || getResp.status === 403) {
        localStorage.removeItem('github_pat');
        token = askToken();
        getResp = await fetch(apiBase, {
          headers: { Authorization: 'token ' + token, Accept: 'application/vnd.github.v3+json' }
        });
      }
      if (getResp.status === 403 || getResp.status === 404) {
        const repoCfg = askRepoConfig();
        owner = repoCfg.owner;
        repo = repoCfg.repo;
        apiBase = 'https://api.github.com/repos/' + owner + '/' + repo + '/contents/' + filePath;
        getResp = await fetch(apiBase, {
          headers: { Authorization: 'token ' + token, Accept: 'application/vnd.github.v3+json' }
        });
      }
      if (!getResp.ok) {
        const detail = await readGitHubError(getResp);
        throw new Error('讀取 learning.json 失敗 (' + getResp.status + ')' + detail);
      }
      const fileData = await getResp.json();
      const sha = fileData.sha;

      // Decode UTF-8 base64
      const raw = atob(fileData.content.replace(/\n/g, ''));
      const rawBytes = new Uint8Array(raw.length);
      for (let i = 0; i < raw.length; i++) rawBytes[i] = raw.charCodeAt(i);
      const vocab = JSON.parse(new TextDecoder('utf-8').decode(rawBytes));

      // SRS intervals: index = reviewCount after correct answer
      const SRS = [1, 3, 7, 14, 30, 60, 90];

      for (const r of results) {
        const w = vocab.words.find(x => x.word === r.word);
        if (!w || w.lastReviewedDate === today) continue; // skip if already reviewed today
        w.lastReviewedDate = today;
        const next = new Date();
        if (r.correct) {
          w.reviewCount = (w.reviewCount || 0) + 1;
          next.setDate(next.getDate() + (SRS[Math.min(w.reviewCount, SRS.length - 1)] || 90));
        } else {
          w.reviewCount = 0;
          next.setDate(next.getDate() + 1); // wrong: reset, review tomorrow
        }
        w.nextReview = next.toISOString().slice(0, 10);
      }

      // Encode to UTF-8 base64
      const newJson = JSON.stringify(vocab, null, 2);
      const newBytes = new TextEncoder().encode(newJson);
      let binary = '';
      newBytes.forEach(b => binary += String.fromCharCode(b));
      const encoded = btoa(binary);

      const putWithSha = (currentSha, currentToken) => fetch(apiBase, {
        method: 'PUT',
        headers: { Authorization: 'token ' + currentToken, 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: 'SRS update: review quiz ' + today, content: encoded, sha: currentSha })
      });

      let putResp = await putWithSha(sha, token);
      if (putResp.status === 401 || putResp.status === 403) {
        localStorage.removeItem('github_pat');
        token = askToken();

        const latestResp = await fetch(apiBase, {
          headers: { Authorization: 'token ' + token, Accept: 'application/vnd.github.v3+json' }
        });
        if (!latestResp.ok) {
          const detail = await readGitHubError(latestResp);
          throw new Error('重新取得檔案失敗 (' + latestResp.status + ')' + detail);
        }
        const latestData = await latestResp.json();
        putResp = await putWithSha(latestData.sha, token);
      }
      if (!putResp.ok) {
        const detail = await readGitHubError(putResp);
        throw new Error('更新失敗 (' + putResp.status + ')' + detail);
      }

      localStorage.setItem(storageKey, '1');
      resultEl.innerHTML = '🎉 複習完成！' + score + '/' + results.length + ' 題答對，SRS 記錄已更新 ✅';
      convertElementToSimplified(resultEl);
      resultEl.className = (score === results.length) ? 'success' : 'partial';
      resultEl.style.display = 'block';
      submitBtn.textContent = '✅ 已同步';

    } catch (err) {
      items.forEach(item => {
        const prev = selectedByWord[item.dataset.word];
        item.querySelectorAll('.rq-opt').forEach(b => {
          b.removeAttribute('disabled');
          b.classList.remove('correct', 'wrong', 'selected');
          if (prev && b.dataset.val === prev) b.classList.add('selected');
        });
      });
      submitBtn.disabled = false;
      submitBtn.textContent = '提交答案 & 保存 SRS 記錄';
      alert('同步失敗：' + err.message);
    }
  }

  // Hide submit button if no review quiz items
  document.addEventListener('DOMContentLoaded', () => {
    const articleAudio = document.getElementById('article-audio');
    const articleSrc = buildAssetUrl('article.mp3');
    articleAudio.src = articleSrc;
    articleAudio.preload = 'metadata';
    articleAudio.load();

    syncSentenceModeButtons();
    refreshRepoTargetHint();
    const repoHint = document.getElementById('repo-target-hint');
    const repoEditBtn = document.getElementById('repo-target-edit-btn');
    const localExportBtn = document.getElementById('local-export-btn');
    const localImportBtn = document.getElementById('local-import-btn');
    const localStoreInfo = document.getElementById('local-store-info');
    if (REVIEW_SYNC_MODE === 'local') {
      if (repoHint) repoHint.textContent = '当前模式：自动本地保存（无需 GitHub / 无需导入导出）';
      if (repoEditBtn) repoEditBtn.style.display = 'none';
      if (localExportBtn) localExportBtn.style.display = 'none';
      if (localImportBtn) localImportBtn.style.display = 'none';
      refreshLocalStoreInfo();
      const submitBtn = document.getElementById('rq-submit-btn');
      if (submitBtn) submitBtn.textContent = '提交答案 & 保存 SRS 記錄';
    }
    if (!document.querySelector('.rq-item')) {
      const btn = document.getElementById('rq-submit-btn');
      if (btn) btn.style.display = 'none';
      const editBtn = document.getElementById('repo-target-edit-btn');
      if (editBtn) editBtn.style.display = 'none';
      const exportBtn = document.getElementById('local-export-btn');
      if (exportBtn) exportBtn.style.display = 'none';
      const importBtn = document.getElementById('local-import-btn');
      if (importBtn) importBtn.style.display = 'none';
      if (localStoreInfo) localStoreInfo.style.display = 'none';
    }
    applySimplifiedChinese();
  });

  // Loop playback toggle
  function toggleLoop(btn) {
    const audio = document.getElementById('article-audio');
    audio.loop = !audio.loop;
    btn.classList.toggle('active', audio.loop);
  }

  // Speaking Bridge reveal toggle
  function bridgeReveal(btn) {
    const ans = btn.nextElementSibling;
    if (ans.style.display === 'block') {
      ans.style.display = 'none';
      btn.textContent = btn.textContent.replace('隱藏', '顯示');
    } else {
      ans.style.display = 'block';
      btn.textContent = btn.textContent.replace('顯示', '隱藏');
    }
  }

  // Vocab, Review & Phrase data
  const VOCAB = {
    // '[word]': { pos:'n.', zh:'中文', example:'例句' },
    [VOCAB_DATA]
  };
  const REVIEW = {
    // '[word]': { pos:'n.', zh:'中文', example:'例句' },
    [REVIEW_DATA]
  };
  const PHRASES = {
    // '[phrase]': { zh:'中文', note:'文章用法說明', type:'Phrasal Verb' },
    [PHRASE_DATA]
  };

  // Popup
  const popup = document.getElementById('word-popup');
  const popContent = document.getElementById('pop-content');
  const defCache = {};
  let _anchor = null;

  function showPopup(word, anchorEl, type) {
    _anchor = anchorEl;
    popContent.innerHTML = '';
    const key = word.toLowerCase();
    if (type === 'vocab' && VOCAB[key]) {
      const v = VOCAB[key];
      popContent.innerHTML = `<div class="pop-word">${word} <span class="pop-badge vocab">今日單字</span></div>
        <span class="pop-badge" style="margin:.2rem 0 .3rem;display:inline-block">${v.pos}</span>
        <div class="pop-example">"${v.example}"</div>
        <button class="pop-zh-btn" onclick="revealZh(this)">👁 看中文翻譯</button>
        <div class="pop-zh" style="display:none">${v.zh}</div>`;
    } else if (type === 'review' && REVIEW[key]) {
      const rv = REVIEW[key];
      popContent.innerHTML = `<div class="pop-word">${word} <span class="pop-badge review">複習單字</span></div>
        <span class="pop-badge" style="margin:.2rem 0 .3rem;display:inline-block">${rv.pos}</span>
        <div class="pop-example">"${rv.example}"</div>
        <button class="pop-zh-btn" onclick="revealZh(this)">👁 看中文翻譯</button>
        <div class="pop-zh" style="display:none">${rv.zh}</div>`;
    } else if (type === 'phrase' && PHRASES[key]) {
      const ph = PHRASES[key];
      popContent.innerHTML = `<div class="pop-word">${word} <span class="pop-badge phrase">片語</span></div>
        <span class="pop-type-badge">${ph.type}</span>
        <div class="pop-note">${ph.note}</div>
        <button class="pop-zh-btn" onclick="revealZh(this)">👁 看中文</button>
        <div class="pop-zh" style="display:none">${ph.zh}</div>`;
    } else {
      popContent.innerHTML = `<div class="pop-word">${word}</div><div class="pop-loading">查詢中…</div>`;
      convertElementToSimplified(popContent);
      fetchDef(key).then(html => { popContent.innerHTML = html; convertElementToSimplified(popContent); positionPopup(anchorEl); });
    }
    convertElementToSimplified(popContent);
    popup.style.display = 'block';
    positionPopup(anchorEl);
  }

  function revealZh(btn) {
    btn.nextElementSibling.style.display = 'block';
    btn.style.display = 'none';
    if (_anchor) positionPopup(_anchor);
  }

  function positionPopup(el) {
    const r = el.getBoundingClientRect();
    const pw = popup.offsetWidth || 260, ph = popup.offsetHeight || 120;
    let left = r.left;
    let top = r.bottom + 8;
    if (left + pw > window.innerWidth - 12) left = window.innerWidth - pw - 12;
    if (left < 12) left = 12;
    if (r.bottom + ph + 8 > window.innerHeight) top = r.top - ph - 8;
    if (top < 8) top = 8;
    popup.style.left = left + 'px';
    popup.style.top = top + 'px';
  }

  function closePopup() { popup.style.display = 'none'; }

  async function fetchDef(word) {
    if (defCache[word]) return defCache[word];
    try {
      const res = await fetch(`https://api.dictionarapi.dev/api/v2/entries/en/${word}`);
      if (!res.ok) throw new Error();
      const data = await res.json();
      const entry = data[0];
      const meanings = entry.meanings.slice(0,2).map(m => {
        const def = m.definitions[0];
        const ex = def.example ? `<div class="pop-example">"${def.example}"</div>` : '';
        return `<div style="margin-top:.4rem"><span class="pop-badge">${m.partOfSpeech}</span><div class="pop-def">${def.definition}</div>${ex}</div>`;
      }).join('');
      const html = `<div class="pop-word">${entry.word}</div>${meanings}`;
      return defCache[word] = html;
    } catch {
      return defCache[word] = `<div class="pop-word">${word}</div><div class="pop-def" style="margin-top:.3rem">查無結果</div>`;
    }
  }

  document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('article-body').addEventListener('click', e => {
      const v  = e.target.closest('.vocab-word');
      const rv = e.target.closest('.review-word');
      const ph = e.target.closest('.phrase-chunk');
      if (v)       showPopup(v.dataset.word,    v,  'vocab');
      else if (rv) showPopup(rv.dataset.word,   rv, 'review');
      else if (ph) showPopup(ph.dataset.phrase, ph, 'phrase');
    });
    document.addEventListener('click', e => {
      if (!popup.contains(e.target) && !e.target.closest('.vocab-word,.review-word,.phrase-chunk')) closePopup();
    });
  });
</script>
</body>
</html>
```

**填寫說明：**
- `[VOCAB_DATA]`：填入今日新單字的 JS 物件，格式：`'word': { pos:'n.', zh:'中文', example:'例句' },`
- `[REVIEW_DATA]`：填入文章中融入的 2–3 個複習單字資料，從 learning.json 讀取對應欄位，格式同 VOCAB_DATA：`'word': { pos:'n.', zh:'中文', example:'例句' },`
- `[PHRASE_DATA]`：填入所有片語的 JS 物件，格式：`'go through': { zh:'通過', note:'文章用法：go through security → 通過安檢', type:'Phrasal Verb' },`
  - `type` 只能是 `'Phrasal Verb'`、`'Collocation'`、`'Fixed Expression'` 三者之一
- 文章中的 `vocab-word` span 的 `data-word` 要與 VOCAB 的 key 完全一致（小寫）
- 文章中的 `review-word` span 的 `data-word` 要與 REVIEW 的 key 完全一致（小寫）
- 文章中的 `phrase-chunk` span 的 `data-phrase` 要與 PHRASES 的 key 完全一致
- `[REVIEW_QUIZ_HTML]`：針對 3e 找到的所有到期複習單字（排除 reviewCount >= 7），每個出一題。每題 4 個選項（1 正確 + 3 干擾），隨機排序。格式：
  ```html
  <div class="rq-item" data-word="exhausted" data-correct="exhausted">
    <div class="rq-zh">筋疲力盡的 <span class="rq-pos">adj.</span></div>
    <div class="rq-hint">I was ____ after the long flight.</div>
    <div class="rq-opts">
      <button class="rq-opt" data-val="routine" onclick="rqSelect(this)">routine</button>
      <button class="rq-opt" data-val="exhausted" onclick="rqSelect(this)">exhausted</button>
      <button class="rq-opt" data-val="elevator" onclick="rqSelect(this)">elevator</button>
      <button class="rq-opt" data-val="budget" onclick="rqSelect(this)">budget</button>
    </div>
  </div>
  ```
  `.rq-hint` 是從 learning.json 的 `exampleSentence` 取得，將目標單字替換成 `____`（複數形如 errands → ____s 時連 s 也要保留在 ____ 後）。
  若無到期複習單字，填入：`<div class="review-msg">今天沒有需要複習的單字！繼續保持 💪</div>`

---

### Step 5：產生語音檔

用 edge-tts 產生 MP3。需要產生兩種檔案：
1. `article.mp3`：整篇文章完整朗讀
2. `s01.mp3`, `s02.mp3`, ...：每個句子個別朗讀（對應 Step 4 中 data-idx 的編號）

**SENTENCES 陣列**：將文章每個句子依序列出純文字（順序必須與 HTML 中 data-idx 完全一致）：

```python
import asyncio, edge_tts

FOLDER = "./daily/[TODAY 替換成今天日期]"
VOICE = "en-US-JennyNeural"
RATE = "-10%"

SENTENCES = [
    "[S1 純文字]",
    "[S2 純文字]",
    "[S3 純文字]",
    # ... 所有句子
]

async def gen(text, path):
    c = edge_tts.Communicate(text, voice=VOICE, rate=RATE)
    await c.save(path)

async def main():
    # 完整文章
    full_text = " ".join(SENTENCES)
    await gen(full_text, f"{FOLDER}/article.mp3")
    # 个別句子
    for i, sent in enumerate(SENTENCES, 1):
        await gen(sent, f"{FOLDER}/s{i:02d}.mp3")

asyncio.run(main())
```

将上方程式碼寫入 `/tmp/tts_today.py`，然後執行：
```bash
python3 /tmp/tts_today.py
```

---

### Step 6：更新資料檔案

更新 `./vocabulary/learning.json`：
- 把今日 **3 個**新單字加入 words 陣列
- 每個單字格式：
```json
{
  "word": "example",
  "partOfSpeech": "n.",
  "chineseMeaning": "例子",
  "exampleSentence": "This is an example.",
  "dateAdded": "YYYY-MM-DD",
  "reviewCount": 0,
  "nextReview": "YYYY-MM-DD",
  "lastReviewedDate": null
}
```

**`nextReview` 計算規則（Spaced Repetition 科學間隔）：**

| reviewCount | 下次複習間隔 | 說明 |
|-------------|------------|------|
| 0（初次加入） | 今天 + 1 天 | 新增時設定 |
| 1 | 今天 + 3 天 | |
| 2 | 今天 + 7 天 | |
| 3 | 今天 + 14 天 | |
| 4 | 今天 + 30 天 | |
| 5 | 今天 + 60 天 | |
| 6 | 今天 + 90 天 | |
| ≥ 7 | 不再出現 | 已掌握，從複習佇列移除 |

⚠️ **SRS 更新規則（由瀏覽器 Active Recall Quiz 透過 GitHub API 負責，非排程任務）：**
- 答對：`reviewCount +1`，按上表計算新 `nextReview`，`lastReviewedDate = 今天`
- 答錯：`reviewCount = 0`，`nextReview = 明天`，`lastReviewedDate = 今天`
- 每天只有**第一次**作答才更新 SRS（`lastReviewedDate` 當天重複練習不會改變 SRS）

初次加入的單字：`reviewCount = 0`，`lastReviewedDate = null`，`nextReview = 明天（+1天）`。

更新 `./profile.json`：
- `totalDays` + 1
- `lastUpdated` = 今天日期
- `lastTopic` = 今日主題（`daily` 或 `travel`，必須符合上方固定交替規則）

---

### Step 7：更新首頁清單並上傳 GitHub

#### 7a. 在 `./index.html` 的 `<!-- DAYS_START -->` 與 `<!-- DAYS_END -->` 之間，**最前面**插入今天的項目：

```html
<a class="day-item" href="daily/[日期]/">
  <div class="day-left">
    <div class="day-date">[日期]</div>
    <div class="day-title">[文章標題]</div>
  </div>
  <div class="day-num">Day [累計天數]</div>
</a>
```

新項目要插在舊項目**上方**（最新的在最頂端）。

#### 7b. git commit 並 push：

```bash
PROJECT_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$PROJECT_ROOT"
git add .
git commit -m "Day [N]：[今日文章標題]"
git push
```

commit message 格式：`Day [累計天數]：[文章標題]`
例如：`Day 2：A Morning at the Café`

---

### Step 8：最後輸出摘要

```
✅ 今日學習材料已產生並上傳！

📁 路徑：./daily/[日期]/
🌐 index.html  - 今日學習頁面（含文章、單字、片語、測驗）
🔊 article.mp3 - 語音朗讀
☁️  GitHub     - https://github.com/CarryJone/english-learning

📚 今日新增單字：[列出單字]
🔗 今日片語：[列出片語]
📅 累計學習天數：[N] 天
```
