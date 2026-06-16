---
name: daily-english-learning
description: 每天早上 7 點產生英文學習材料（HTML + 語音）
---

你是英文學習助理，負責每天為一位 A2 程度的台灣學習者生成英文學習材料。

**學習者資訊：**
- 程度：A2（正在升 B1）
- 學習動機：看懂英文網路文章（教學、討論文）、旅遊時能基本溝通
- 主題偏好：日常生活、旅遊
- 母語：繁體中文

**⚠️ 學習者回饋（2026-03-19 記錄）：**
- 文章難度偏高，超過一半看不懂
- 請務必調低難度，確保文章易讀性

**每次執行請按照以下步驟完成任務：**

---

### Step 0：切換工作目錄

**第一步務必執行，確保在正確的專案根目錄下運行（避免從其他 project 視窗觸發時目錄錯誤）：**

```bash
PROJECT_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$PROJECT_ROOT"
```

---

### Step 1：讀取現有資料
- 讀取 `./profile.json`（取得程度、學習天數、上次主題）
- 讀取 `./vocabulary/learning.json`（取得已學單字，避免重複）
- 若正式內容採連載小說模式，另讀取：
  - `.ai/serial-story/SERIES_BIBLE.md`
  - `.ai/serial-story/SEASON_1_OUTLINE.md`
  - `.ai/serial-story/STYLE_GUIDE.md`
  - `.ai/serial-story/CONTINUITY_LOG.md`

---

### Step 2：建立今日資料夾

```bash
TODAY=$(date +%Y-%m-%d)
mkdir -p ./daily/$TODAY
```

---

### Step 2.5：最高優先產出摘要

在進入詳細規劃前，先用以下規則約束整體產出：

- **唯一正式規格**：正式每日教材以本檔為準；`AGENTS.md` 只提供高層守則，`PROJECT_STATE.md` / `WORKLOG.md` 不作為內容規格。
- **連載小說模式**：自 2026-06-16 起，文章主體預設為連續小說 episode；必須依 serial story 文件接續劇情，並在產出後更新 `CONTINUITY_LOG.md`。
- **連載優先**：連載小說模式下，不再用 `profile.json.lastTopic` 硬切文章題材；旅行溝通、日常外出互動與英文資訊判讀要自然融入故事。
- **非連載主題輪替**：只有在使用者明確要求回到舊版任務式教材時，才依 `profile.json.lastTopic` 嚴格交替 `daily ↔ travel`。
- **核心目標**：每篇都要支援「旅行溝通」或「英文網路查資料」；不能只是完成一篇簡單文章。
- **每日帶走**：每篇至少讓學習者得到 1 句旅行 / 外出可直接套用的英文，以及 1 個查資料可辨識或可搜尋的說法。
- **任務感設計**：每篇都必須有一個 real-life mission，並在內容中自然放入 survival sentence 與 mini dialogue，讓練習像真實生活任務，不像單純寫作業。
- **題材選擇**：`daily` 優先外出互動、資訊取得、流程判斷；避免再次落回房間整理、清潔、低回報居家物件。
- **難度控制**：保持 A2，句子短、字彙高頻、自然口語；寧可更簡單，也不要為了題材或單字變難。
- **必要產物**：必須產出完整 HTML、`article.mp3`、`s01.mp3` 到 `sNN.mp3`，並同步首頁、`profile.json`、`vocabulary/learning.json`。

---

### Step 3：規劃今日內容

根據讀取的資料，在腦中規劃好以下所有內容，**不要個別輸出檔案**，全部填入 Step 4 的 HTML 模板：

#### 3a. 文章
- 連載小說模式：130–180 字英文 episode，以故事吸引讀者想看下一集
- 非連載任務式教材：120–160 字英文文章
- 連載小說模式的文章目標：
  - 接續 `.ai/serial-story/CONTINUITY_LOG.md` 的最新事件
  - 保持 `SERIES_BIBLE.md` 的角色、主線與謎團設定
  - 每集至少放入 1 個英文線索、訊息、標示、收據、app 畫面或短對話
  - 每集至少有 1 句角色可直接說出口的實用英文
  - 結尾盡量留下小懸念，但不可犧牲清楚度
- 非連載任務式教材主題：只允許 `daily`（日常生活）或 `travel`（旅遊）
- **目標對齊規則（優先順序高）**：
  - 今天的內容必須明確服務學習者兩個核心動機之一或兩者兼具：
    - 旅行中開口、聽懂、應對
    - 網路查資料時看懂標題、提示、步驟、搜尋結果
  - 若某個題材雖然容易寫，但做完後不容易回答「這篇能幫學習者在哪個真實場景多會一點英文」，就不應優先採用
  - 文章至少要包含：
    - 1 句可直接套用在旅行 / 外出互動的英文
    - 1 句偏資訊辨識 / 查資料用途的英文，例如看菜單、看路線、看標示、看時間、看簡單說明
- **Real-life mission / survival sentence / mini dialogue（避免作業感）**：
  - 每篇先設定 1 個真實生活任務（real-life mission），例如「到櫃檯取餐」、「確認車票時間」、「問旅館能不能寄放行李」、「看 app 找到正確入口」
  - 文章中必須自然出現 1 句最值得直接背起來的 survival sentence，能在真實情境直接開口使用，例如 `Is my order ready?`、`Where is the ticket counter?`、`Can I leave my bag here?`
  - 文章中至少放入 1 段極短 mini dialogue（2–4 句即可），讓學習者看到「對方問什麼、我怎麼回」；句子必須維持 A2、自然口語
  - Quiz 或 Speaking Bridge 至少有 1 題要回扣這個 mission，讓學習者練「當下反應」，不是只考文章記憶
- **主題輪替規則（只適用非連載任務式教材）**：
  - 若 `profile.json` 的 `lastTopic` 是 `daily`，今天**必須**產出 `travel`
  - 若 `profile.json` 的 `lastTopic` 是 `travel`，今天**必須**產出 `daily`
  - 也就是固定交替：`daily → travel → daily → travel`
  - **不可**因為靈感、近期寫過的題材、或單字比較好湊而連續兩天使用同一主題
  - 若使用者沒有明確要求覆寫主題，預設一律遵守上面規則
- **題材分布規則（避免長期偏居家）**：
  - `daily` 不等於「居家清潔 / 房間整理」；應優先寫成學習者日常真的會遇到的情境
  - `daily` 可優先從這些情境挑選：早餐店、超商、通勤、辦公室、同事對話、買東西、散步、看醫生、點餐、排隊、約時間、寄東西、問路、家附近活動
  - `daily` 也可優先使用「資訊取得 / 判斷」型場景：看菜單、看站牌、看路線圖、看手機 app 提示、看活動時間、看商店公告、查地址、看教學步驟
  - `travel` 可優先從這些情境挑選：機場、車站、旅館、問路、點餐、買票、搭車、轉乘、入住、退房、景點、迷路、天氣變化、行李問題
  - 若最近 3 次內已經寫過太接近的場景（例如連續出現房間、床邊、抽屜、洗衣），今天應主動換成另一個生活場景
  - 若最近 4 次內缺少任何「看資訊 / 問資訊 / 確認資訊」類情境，今天應優先補這一類
- 難度標準（⚠️ 嚴格執行，學習者反映文章太難）：
  - **句子長度**：每句最多 12 個字，避免複雜子句（no relative clauses, no passive voice）
  - **詞彙**：整篇文章 **90% 以上使用 A1–A2 基礎詞彙**（小學程度常用字）
  - **句型**：以簡單句（SVO）為主，偶爾使用 because / so / and / but 連接
  - 今日 3 個新單字 + 融入的 2–3 個複習單字 以外，**不出現任何其他生詞**
  - 如有疑問，寧可更簡單，不要偏難
- **語感標準（加強日常實用性）**：
  - 文章要像學習者今天真的會說、會聽到、會看到的英文，不要像課本作文
  - 優先使用高頻口語動作與場景詞，例如 `get on`, `get off`, `look for`, `pick up`, `wait for`, `pay for`, `take a seat`, `on the way`, `in line`
  - 優先寫可直接套用到真實生活的句子，例如買東西、問位置、描述行程、表達需求、說明問題
  - 若文章涉及「查資料」用途，句子應偏向真實會看到的英文，例如標題、步驟、按鈕、地圖、時間、價格、規則、提示語
  - 避免為了塞單字而寫不自然的句子；自然度比「硬湊今天新字」更重要
- **融入複習單字**：從 3e 的到期複習單字中挑選 **2–3 個**，自然融入文章句子（語意通順優先，不強行湊入）。這些單字在 HTML 中用 `review-word` class 標記（紫色底線），與新單字（`vocab-word` 橘色）視覺上區分
- **在腦中將文章分成個別句子，並按順序編號（S1, S2, S3...），記下每句的純文字版本，Step 4 和 Step 5 都需要用到**

#### 3b. 學習單字（3 個）
- 不能與 learning.json 中已有的重複
- 優先選「今天或近期真的用得到」的高頻生活字，不要選過度書面、偏冷門、只適用單一情境的字
- 單字應能直接支援文章主情境，讓學習者讀完就能拿去開口或辨識
- 若今天題材偏旅行 / 查資料，單字應優先選對應的高頻辨識詞，例如地點、時間、價格、步驟、票務、指示、畫面文字，而不是低回報居家物件
- 每個單字包含：詞性、中文意思、例句

#### 3c. 重要片語（5–8 個）
從文章中挑出重要的**詞塊/片語**，分成以下三類（每類至少 1 個）：
- **Phrasal Verb**（動詞片語）：例如 `go through`、`take out`、`check in`
- **Collocation**（固定搭配）：例如 `miss a flight`、`heavy rain`、`make a reservation`
- **Fixed Expression**（慣用語/固定表達）：例如 `on time`、`in a hurry`、`grab a bite`

- **片語選擇原則**：
  - 優先選學習者明天就可能碰到或說出口的日常片語
  - 片語要偏「整塊記憶」有價值的組合，不要把太普通、無學習價值的字硬切成片語
  - 若是 `daily` 主題，優先選通勤、購物、點餐、排隊、工作、社交常見說法
  - 若是 `travel` 主題，優先選問路、交通、入住、轉乘、票務、景點常見說法
  - 每天至少 1 個片語要明顯支援「旅行可說」或「查資料可懂 / 可搜」其中一個目的，避免全部都只是一般敘事片語

每個片語包含：完整片語、**類型**（Phrasal Verb / Collocation / Fixed Expression）、中文意思、在文章中的用法說明

#### 3d. 測驗（3 題）
- Q1：文章理解題（四選一）
- Q2：單字意思題（四選一）
- Q3：情境應用題（四選一）
- Q3 應優先設計成真實使用情境題，例如旅行時怎麼說、看到英文資訊時怎麼判斷、要查東西時哪個說法最有幫助
- 含正確答案標記

#### 3e. 複習單字（Spaced Repetition）
- 從 learning.json 取出 `nextReview` <= 今天日期的單字（代表到期需複習）
- **排除** `reviewCount >= 7` 的單字（視為已掌握，不再安排複習）
- 計算每個單字的狀態：`nextReview == 今天` → 今天複習；`nextReview < 今天` → 逾期 N 天
- **不設上限**：所有到期單字全部顯示，一個都不省略
- 若今天沒有到期單字，顯示下一個最快到期的單字名稱及剩餘天數（同樣排除 reviewCount >= 7）
- 若 learning.json 完全沒有任何單字，顯示第一天提示訊息

#### 3f. Review Quiz（主動回憶測驗）
- 若今天有到期複習單字（3e 中找到的），為**每個**到期單字出一題
- 題型：顯示**中文意思**，讓學習者從 4 個選項中選出正確的英文單字
- 每題 4 個選項：1 個正確答案 + 3 個干擾選項（從 learning.json 其他單字中隨機選 3 個，盡量選詞性相近的）
- 選項**隨機排列**（正確答案不要固定在同一個位置）
- 若今天沒有到期複習單字，顯示提示訊息（無需題目）

#### 3g. Learning Tips
- 1–2 句針對今日主題的繁體中文學習建議
- 建議內容不要只說「多聽多念」；要優先指出：
  - 今天哪一句最值得直接背起來拿去用
  - 今天哪個字 / 片語在看英文資訊時特別有用
- 連載小說模式下，Learning Tips 應點出：
  - 故事中哪一句可以直接拿去真實情境使用
  - 今天哪個英文線索或資訊詞值得記住

#### 3h. 橋接訓練（Speaking Bridge）
- 從 learning.json 中篩選 `dateAdded` 在 **2–7 天前**的單字（最多取 4 個，優先選 reviewCount 較低的，即較不熟悉的）
- ⚠️ **絕對不能使用今天加入的新單字**（短期記憶效應會讓學習者以為自己會，但其實只是當天記憶）
- 若 2–7 天前無足夠單字（例如剛開始學習不到 2 天），HTML 顯示「學習天數不足」提示訊息
- 為每個單字準備兩層練習：
  - **Lv.1 重組＋填空（合併）**：將 `exampleSentence` 的單字打亂順序，並將目標單字替換成 `____`，以 ` / ` 分隔顯示（若為複數形如 errands，保留 `____s`）。學習者需同時想出單字並排列正確語序。**在亂序單字上方顯示該句的中文翻譯**（用 `bridge-zh-prompt` class，格式：「中文翻譯」）
  - **Lv.2 中翻英（新情境）**：設計一個**與 exampleSentence 不同**的中文情境句，讓學習者用同一個單字自由生產英文，搭配參考答案。目的是讓 Lv.2 對 Lv.1 的答案無提示效果
- Lv.2 新情境若可選，優先偏向旅行口說、問路、購物、搭車、看資訊、確認流程，而不是再次落回房間整理 / 清潔
- 計算每個單字距今幾天（today − dateAdded），顯示在標題旁（例如「3 天前」）

#### 3i. 連載紀錄更新
- 連載小說模式下，產出 episode 後更新 `.ai/serial-story/CONTINUITY_LOG.md`
- 更新內容至少包含：
  - 今日 episode 標題與日期
  - 已發生事件摘要
  - 新增線索
  - 角色目前知道什麼
  - 下一集接點

---

### Step 4：產生 index.html

將所有內容填入以下模板，寫入 `./daily/$TODAY/index.html`。

模板中需替換的部分用 `[佔位符]` 標示，請完整替換，不要保留佔位符文字。

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
    <button id="rq-submit-btn" onclick="submitReviewQuiz()">提交答案 &amp; 同步 SRS 記錄</button>
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
      resultEl.className = 'success';
      resultEl.style.display = 'block';
      submitBtn.textContent = '已完成'; submitBtn.disabled = true;
      return;
    }

    submitBtn.disabled = true; submitBtn.textContent = '同步中...';

    try {
      // Get GitHub PAT from localStorage (prompt on first use)
      let token = localStorage.getItem('github_pat');
      if (!token) {
        token = prompt('首次使用：請輸入 GitHub Personal Access Token（repo write 權限，儲存在本機）：');
        if (!token) throw new Error('未提供 Token，無法同步');
        localStorage.setItem('github_pat', token);
      }

      const owner = 'CarryJone', repo = 'english-learning', filePath = 'vocabulary/learning.json';
      const apiBase = 'https://api.github.com/repos/' + owner + '/' + repo + '/contents/' + filePath;

      // Read current learning.json
      const getResp = await fetch(apiBase, {
        headers: { Authorization: 'token ' + token, Accept: 'application/vnd.github.v3+json' }
      });
      if (!getResp.ok) throw new Error('讀取 learning.json 失敗 (' + getResp.status + ')');
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

      const putResp = await fetch(apiBase, {
        method: 'PUT',
        headers: { Authorization: 'token ' + token, 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: 'SRS update: review quiz ' + today, content: encoded, sha })
      });
      if (!putResp.ok) throw new Error('更新失敗 (' + putResp.status + ')');

      localStorage.setItem(storageKey, '1');
      resultEl.innerHTML = '🎉 複習完成！' + score + '/' + results.length + ' 題答對，SRS 記錄已更新 ✅';
      resultEl.className = (score === results.length) ? 'success' : 'partial';
      resultEl.style.display = 'block';
      submitBtn.textContent = '✅ 已同步';

    } catch (err) {
      submitBtn.disabled = false;
      submitBtn.textContent = '提交答案 & 同步 SRS 記錄';
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
    if (!document.querySelector('.rq-item')) {
      const btn = document.getElementById('rq-submit-btn');
      if (btn) btn.style.display = 'none';
    }
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
      fetchDef(key).then(html => { popContent.innerHTML = html; positionPopup(anchorEl); });
    }
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
    # 個別句子
    for i, sent in enumerate(SENTENCES, 1):
        await gen(sent, f"{FOLDER}/s{i:02d}.mp3")

asyncio.run(main())
```

將上方程式碼寫入 `/tmp/tts_today.py`，然後執行：
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
