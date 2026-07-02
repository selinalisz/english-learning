# 工作日誌

> 用途：記錄已發生的近期工作事件，最新紀錄放最上方。
> 注意：本檔不是開發規則、不是待辦清單、不是規格來源；不要依本檔決定實作方式。
> 維護：超過 30 筆時，建議歸檔到 `.ai/archive/WORKLOG_YYYY_MM.md`。

---
## 2026-07-02 — Day 69 正式教材產出

- 先 `git fetch origin main` 確認遠端狀態，因 `origin/main` 與本地一致，直接用目前最新的 `vocabulary/learning.json` 生成今日教材。
- 延續 `The Blue Receipt` 主線，新增 `daily/2026-07-02/`，標題為 `The Blue Receipt · Episode 11`。
- 新增單字：`truth`、`alone`、`early`；文章融入複習字：`voice`、`inside`、`outside`。
- 補齊 `article.mp3` 與 `s01.mp3` 到 `s25.mp3`，並同步首頁、`profile.json`、`vocabulary/learning.json`、`.ai/PROJECT_STATE.md`、`.ai/serial-story/CONTINUITY_LOG.md`。
- 驗證：句子編號連續、25 個單句音檔存在、Review Quiz 11 題、Speaking Bridge 4 題、本機 HTTP 200。

---
## 2026-07-01 — Day 68 正式教材產出

- 先 `git fetch origin main`，確認遠端多了 `SRS update: review quiz 2026-06-30` 後，再 `git pull --ff-only origin main` 同步最新 `vocabulary/learning.json`。
- 延續 `The Blue Receipt` 主線，新增 `daily/2026-07-01/`，標題為 `The Blue Receipt · Episode 10`。
- 新增單字：`voice`、`inside`、`outside`；文章融入複習字：`paper`、`date`、`tomorrow`。
- 補齊 `article.mp3` 與 `s01.mp3` 到 `s25.mp3`，並同步首頁、`profile.json`、`vocabulary/learning.json`、`.ai/PROJECT_STATE.md`、`.ai/serial-story/CONTINUITY_LOG.md`。
- 驗證：句子編號連續、25 個單句音檔存在、Review Quiz 5 題、Speaking Bridge 4 題、本機 HTTP 200。

---
## 2026-06-30 — Day 67 正式教材產出

- 先 `git fetch origin main`，確認遠端多了 `SRS update: review quiz 2026-06-29` 後，再 `git pull --ff-only origin main` 同步最新 `vocabulary/learning.json`。
- 延續 `The Blue Receipt` 主線，新增 `daily/2026-06-30/`，標題為 `The Blue Receipt · Episode 9`。
- 新增單字：`paper`、`date`、`tomorrow`；文章融入複習字：`result`、`history`、`match`。
- 補齊 `article.mp3` 與 `s01.mp3` 到 `s25.mp3`，並同步首頁、`profile.json`、`vocabulary/learning.json`、`.ai/PROJECT_STATE.md`、`.ai/serial-story/CONTINUITY_LOG.md`。
- 驗證：句子編號連續、25 個單句音檔存在、Review Quiz 3 題、Speaking Bridge 4 題、本機 HTTP 200。

---
## 2026-06-29 — Day 66 正式教材產出

- 先 `git fetch --all --prune` 同步遠端狀態，確認本地 `HEAD` 與 `origin/main` 一致後再生成今日教材。
- 延續 `The Blue Receipt` 主線，新增 `daily/2026-06-29/`，標題為 `The Blue Receipt · Episode 8`。
- 新增單字：`result`、`history`、`match`；文章融入複習字：`folder`、`photo`、`record`。
- 補齊 `article.mp3` 與 `s01.mp3` 到 `s25.mp3`，並同步首頁、`profile.json`、`vocabulary/learning.json`、`.ai/PROJECT_STATE.md`、`.ai/serial-story/CONTINUITY_LOG.md`。
- 驗證：句子編號連續、25 個單句音檔存在、Review Quiz 65 題、Speaking Bridge 4 題、本機 HTTP 200。

---
## 2026-06-17 — Day 60 連載小說 Episode 2

- 先 `git fetch --all --prune` / `git pull --ff-only` 同步遠端 `vocabulary/learning.json`，避免用過期 SRS 生成今日 review。
- 延續 `The Blue Receipt` 主線，新增 `daily/2026-06-17/`，標題為 `The Blue Receipt · Episode 2`。
- 新增單字：`listed`、`nearby`、`block`；文章融入複習字：`bottom`、`printed`、`warning`。
- 補齊 `article.mp3` 與 `s01.mp3` 到 `s17.mp3`，並同步首頁、`profile.json`、`vocabulary/learning.json`、`.ai/PROJECT_STATE.md`、`.ai/serial-story/CONTINUITY_LOG.md`。
- 驗證：句子編號連續、17 個單句音檔存在、Review Quiz 3 題、首頁條目存在、本機 HTTP 200。

---
## 2026-06-10 — Day 56 今日英文練習產出

- 同步遠端 `vocabulary/learning.json` 後，依 `profile.json.lastTopic = travel` 產出 daily 主題。
- 新增 `daily/2026-06-10/`，主題 `Reading a Lunch Combo Sign`，包含完整 HTML、`article.mp3` 與 `s01.mp3` 到 `s18.mp3`。
- 新增單字：`combo`、`sauce`、`allergy`；文章融入複習字：`errand`、`payment`、`section`。
- 更新首頁清單、`profile.json`、`vocabulary/learning.json` 與 `.ai/PROJECT_STATE.md`。
- 驗證：HTML 區塊完整、句子編號連續、18 個單句音檔存在、本機 HTTP 200。

---
## 2026-06-09 — Day 55 今日英文練習產出

- 同步遠端 `vocabulary/learning.json` 後，依 `profile.json.lastTopic = daily` 產出 travel 主題。
- 新增 `daily/2026-06-09/`，主題 `Reading the Shuttle Zone Sign`，包含完整 HTML、`article.mp3` 與 `s01.mp3` 到 `s18.mp3`。
- 新增單字：`terminal`、`zone`、`direction`；文章融入複習字：`shuttle`、`staff`、`ready`。
- 更新首頁清單、`profile.json`、`vocabulary/learning.json` 與 `.ai/PROJECT_STATE.md`。
- 驗證：HTML 區塊完整、句子編號連續、18 個單句音檔存在、本機 HTTP 200。

---
## 2026-06-08 — Day 54 今日英文練習產出

- 同步遠端 `vocabulary/learning.json` 後，依 `profile.json.lastTopic = travel` 產出 daily 主題。
- 新增 `daily/2026-06-08/`，主題 `Reloading a Bus Card`，包含完整 HTML、`article.mp3` 與 `s01.mp3` 到 `s18.mp3`。
- 新增單字：`reload`、`balance`、`payment`；文章融入複習字：`queue`、`minute`、`ready`。
- 更新首頁清單、`profile.json`、`vocabulary/learning.json` 與 `.ai/PROJECT_STATE.md`。
- 驗證：HTML 區塊完整、句子編號連續、18 個單句音檔存在、本機 HTTP 200。

---
## 2026-06-04 — Day 52 今日英文練習產出

- 同步遠端 `vocabulary/learning.json` 後，依 `profile.json.lastTopic = travel` 產出 daily 主題。
- 新增 `daily/2026-06-04/`，主題 `Checking a Food Court Pickup Screen`，包含完整 HTML 與 19 個逐句音檔。
- 新增單字：`ready`、`queue`、`section`；文章融入複習字：`special`、`spicy`、`mild`。
- 更新首頁清單、`profile.json`、`vocabulary/learning.json` 與 `.ai/PROJECT_STATE.md`。
- 驗證：HTML 區塊完整、句子編號連續、音檔存在、本機 HTTP 200、Playwright 載入成功且 console 無錯誤。

---
## 2026-05-29 — Day 48 今日英文練習產出

- 同步遠端 `vocabulary/learning.json` 後，依 `profile.json.lastTopic = travel` 產出 daily 主題。
- 新增 `daily/2026-05-29/`，主題 `Reading a Lunch Menu Board`，包含完整 HTML 與 16 個逐句音檔。
- 新增單字：`special`、`spicy`、`mild`；文章融入複習字：`coupon`、`cashier`、`total`。
- 更新首頁清單、`profile.json`、`vocabulary/learning.json` 與 `.ai/PROJECT_STATE.md`。
- 驗證：JSON parse、句子編號、Review Quiz 6 題、瀏覽器載入、HTTP 200、音檔存在。

---
## 2026-05-28 — Day 47 今日英文練習產出

- 同步遠端 `vocabulary/learning.json` 後，依 `profile.json.lastTopic = daily` 產出 travel 主題。
- 新增 `daily/2026-05-28/`，主題 `Reading a Subway Exit Map`，包含完整 HTML 與 17 個逐句音檔。
- 新增單字：`subway`、`exit`、`escalator`；文章融入複習字：`ticket`、`machine`、`direct`。
- 更新首頁清單、`profile.json`、`vocabulary/learning.json` 與 `.ai/PROJECT_STATE.md`。
- 驗證：JSON parse、句子編號、Review Quiz 12 題、瀏覽器載入、HTTP 200、音檔存在。

## 2026-05-21
- 完成：先同步遠端 `vocabulary/learning.json`，再新增 Day 43 正式英文學習材料 `Checking the Train Board`，主題為 travel，任務是先看車站出發看板確認直達車月台，再到資訊櫃台開口詢問是否可暫放行李。
- 修改：`daily/2026-05-21/`、`index.html`、`profile.json`、`vocabulary/learning.json`、`.ai/PROJECT_STATE.md`、`.ai/WORKLOG.md`

---
## 2026-05-20
- 完成：先同步遠端 `vocabulary/learning.json`，再新增 Day 42 正式英文學習材料 `Reading Laundry Room Signs`，主題為 daily，任務是看懂洗衣間告示與付款方式，並現場確認機器是否收卡。
- 修改：`daily/2026-05-20/`、`index.html`、`profile.json`、`vocabulary/learning.json`、`.ai/PROJECT_STATE.md`、`.ai/WORKLOG.md`

---
## 2026-05-19
- 完成：先同步遠端 `vocabulary/learning.json`，再新增 Day 41 正式英文學習材料 `Changing to a Window Seat`，主題為 travel，任務是看懂 app 上的座位資訊與櫃台指示，並在登機門開口換到窗邊座位。
- 修改：`daily/2026-05-19/`、`index.html`、`profile.json`、`vocabulary/learning.json`、`.ai/PROJECT_STATE.md`、`.ai/WORKLOG.md`

---
## 2026-05-18
- 完成：先同步遠端 `vocabulary/learning.json`，再新增 Day 40 正式英文學習材料 `Picking Up a Package`，主題為 daily，任務是看懂取貨 app 提示與取貨碼，並在便利商店 / 取貨櫃台開口領包裹。
- 修改：`daily/2026-05-18/`、`index.html`、`profile.json`、`vocabulary/learning.json`、`.ai/PROJECT_STATE.md`、`.ai/WORKLOG.md`

---
## 2026-05-15
- 完成：先同步遠端 `vocabulary/learning.json`，再新增 Day 39 正式英文學習材料 `Leaving a Bag at the Hotel`，主題為 travel，任務是看懂旅館寄放行李規則並向櫃檯確認是否可保管到晚上。
- 修改：`daily/2026-05-15/`、`index.html`、`profile.json`、`vocabulary/learning.json`、`.ai/PROJECT_STATE.md`、`.ai/WORKLOG.md`

---
## 2026-05-14
- 完成：先同步遠端 `vocabulary/learning.json`，再新增 Day 38 正式英文學習材料 `Reading the Station App`，主題為 daily，任務是看懂站內 app / 告示並向工作人員確認改道後的正確路線。
- 修改：`daily/2026-05-14/`、`index.html`、`profile.json`、`vocabulary/learning.json`、`.ai/PROJECT_STATE.md`、`.ai/WORKLOG.md`

---
## 2026-05-13
- 完成：新增 Day 37 正式英文學習材料 `Finding the Hotel Shuttle`，主題為 travel，任務是看懂接駁集合資訊並向現場人員確認是否搭對車。
- 修改：`daily/2026-05-13/`、`index.html`、`profile.json`、`vocabulary/learning.json`、`.ai/PROJECT_STATE.md`、`.ai/WORKLOG.md`

---
## 2026-05-12
- 完成：新增 Day 36 正式英文學習材料 `Checking Cafe Hours`，主題為 daily，任務是先看店家時間資訊，再到現場等位並確認兩人座位。
- 修改：`daily/2026-05-12/`、`index.html`、`profile.json`、`vocabulary/learning.json`、`.ai/PROJECT_STATE.md`、`.ai/WORKLOG.md`

---
## 2026-05-11
- 完成：新增 Day 35 正式英文學習材料 `Finding the Right Bus Stop`，主題為 travel，任務是在陌生城市看 app / 站牌確認正確公車站並向司機確認方向。
- 修改：`daily/2026-05-11/`、`index.html`、`profile.json`、`vocabulary/learning.json`、`.ai/PROJECT_STATE.md`、`.ai/WORKLOG.md`

---
## 2026-05-08
- 完成：新增 Day 34 正式英文學習材料 `Checking a Return Policy`，主題為 daily，任務是看懂商店退換貨規定並到服務櫃檯詢問換貨。
- 修改：`daily/2026-05-08/`、`index.html`、`profile.json`、`vocabulary/learning.json`、`.ai/PROJECT_STATE.md`、`.ai/WORKLOG.md`

---
## 2026-05-07
- 完成：產出 Day 33 正式英文學習材料，主題為車站置物櫃與看懂費用提示，並同步首頁、profile、SRS 字彙資料與 16 句分句音檔。
- 修改：`daily/2026-05-07/`、`index.html`、`profile.json`、`vocabulary/learning.json`、`.ai/PROJECT_STATE.md`、`.ai/WORKLOG.md`

---
## 2026-05-06
- 完成：新增 Day 32 正式英文學習材料 `Picking Up Medicine`，主題為 daily，任務是到藥局取藥、看號碼與確認櫃檯流程。
- 修改：`daily/2026-05-06/`、`index.html`、`profile.json`、`vocabulary/learning.json`、`.ai/PROJECT_STATE.md`、`.ai/WORKLOG.md`

---
## 2026-05-05
- 完成：新增 Day 31 正式英文學習材料 `Buying a Train Ticket`，主題為 travel，任務是小車站買票與確認月台。
- 修改：`daily/2026-05-05/`、`index.html`、`profile.json`、`vocabulary/learning.json`、`.ai/PROJECT_STATE.md`、`.ai/WORKLOG.md`

---
## 2026-05-04
- 同步 GitHub `main` 後，新增 Day 30 正式英文學習材料 `Checking the Pickup Time`，主題為 daily。
- 更新 `daily/2026-05-04/`、首頁、`profile.json`、`vocabulary/learning.json` 與 `.ai/PROJECT_STATE.md`。

---
## 2026-05-01
- 完成：產出 Day 29 正式英文學習材料，主題為車站找出口與確認路線，並同步首頁、profile、SRS 字彙資料與 16 句分句音檔。
- 修改：`daily/2026-05-01/`、`index.html`、`profile.json`、`vocabulary/learning.json`、`.ai/PROJECT_STATE.md`、`.ai/WORKLOG.md`

## 2026-05-25 — Day 44 今日英文練習產出

- 同步遠端 `vocabulary/learning.json` 後，依 `profile.json.lastTopic = travel` 產出 daily 主題。
- 新增 `daily/2026-05-25/`，主題 `Using a Cafe Coupon`，包含完整 HTML 與 17 個逐句音檔。
- 新增單字：`coupon`、`cashier`、`total`；文章融入複習字：`crowded`、`app`、`code`。
- 更新首頁清單、`profile.json`、`vocabulary/learning.json` 與 `.ai/PROJECT_STATE.md`。
- 驗證：JSON parse、句子編號、HTML placeholder 檢查、HTTP 200、音檔存在與 mp3 header。

---
## 2026-05-26 — Day 45 今日英文練習產出

- 同步遠端 `vocabulary/learning.json` 後，依 `profile.json.lastTopic = daily` 產出 travel 主題。
- 新增 `daily/2026-05-26/`，主題 `Confirming Hotel Breakfast`，包含完整 HTML 與 16 個逐句音檔。
- 新增單字：`breakfast`、`confirm`、`floor`；文章融入複習字：`screen`、`available`、`fee`。
- 更新首頁清單、`profile.json`、`vocabulary/learning.json` 與 `.ai/PROJECT_STATE.md`。
- 驗證：JSON parse、句子編號、Review Quiz 8 題、瀏覽器載入、HTTP 200、音檔存在。

---
## 2026-05-27 — Day 46 今日英文練習產出

- 同步遠端 `vocabulary/learning.json` 後，依 `profile.json.lastTopic = travel` 產出 daily 主題。
- 新增 `daily/2026-05-27/`，主題 `Reading a Self-Checkout Sign`，包含完整 HTML 與 16 個逐句音檔。
- 新增單字：`checkout`、`price`、`wallet`；文章融入複習字：`order`、`available`、`receipt`。
- 更新首頁清單、`profile.json`、`vocabulary/learning.json` 與 `.ai/PROJECT_STATE.md`。
- 驗證：JSON parse、句子編號、Review Quiz 15 題、瀏覽器載入、HTTP 200、音檔存在。

## 2026-06-01 — 產出 Day 49 正式教材

- 先 `git fetch --all --prune` 並 `git pull --ff-only`，同步遠端 `vocabulary/learning.json` 的最新 SRS 更新。
- 依 `profile.json.lastTopic = daily` 產出 `travel` 主題，新增 `daily/2026-06-01/`，標題為 `Checking a Gate Change`。
- 今日新字：`change`、`wrong`、`late`；文章融入複習字：`boarding pass`、`passport`、`gate`。
- Review Quiz / Review Words 依最新 `learning.json` 生成，共納入 45 個到期複習字。
- Speaking Bridge 使用 `confirm`、`exit`、`subway`、`wallet`。
- 驗證：檢查 HTML 結構、JSON 更新、音檔檔案存在與本機 HTTP 200。
## 2026-06-02 — Day 50 正式教材產出

- 先 `git fetch` / `git pull --ff-only` 同步遠端 `vocabulary/learning.json`
- 產出 `daily/2026-06-02/`，主題為 `Reading a Doctor's Message`
- 新增 `article.mp3` 與 `s01.mp3` 到 `s18.mp3`
- 更新首頁清單、`profile.json`、`vocabulary/learning.json`
- 清掉昨天誤重複的 `change` / `wrong` / `late` 三筆 SRS 紀錄
- 驗證：本機瀏覽器載入成功、console 無 error、音檔 HTTP 200、句子與單句音檔數量一致

## 2026-06-03 — Day 51 正式教材產出

- 先 `git fetch` / `git pull --ff-only` 同步遠端 `vocabulary/learning.json`
- 依 `profile.json.lastTopic = daily` 產出 travel 主題，新增 `daily/2026-06-03/`，標題為 `Finding the Airport Bus Bay`
- 今日新字：`bay`、`express`、`staff`；文章融入複習字：`message`、`busy`、`minute`
- 更新首頁清單、`profile.json`、`vocabulary/learning.json` 與 `.ai/PROJECT_STATE.md`
- 驗證：本機頁面載入成功、console 無錯誤、音檔 HTTP 200、句子與單句音檔數量一致

## 2026-06-05 — Day 53 正式教材產出

- 先 `git fetch --all --prune` / `git pull --ff-only` 同步遠端 `vocabulary/learning.json`
- 依 `profile.json.lastTopic = daily` 產出 travel 主題，新增 `daily/2026-06-05/`，標題為 `Checking the Baggage Claim Screen`
- 今日新字：`claim`、`belt`、`hall`；文章融入複習字：`late`、`wrong`、`staff`
- 更新首頁清單、`profile.json`、`vocabulary/learning.json` 與 `.ai/PROJECT_STATE.md`

## 2026-06-12 — Day 57 今日英文練習產出

- 先 `git fetch --all --prune` / `git pull --ff-only` 同步遠端 `vocabulary/learning.json`，避免用過期 SRS 生成 review。
- 依 `profile.json.lastTopic = daily` 產出 `travel` 主題，新增 `daily/2026-06-12/`，標題為 `Reading a Passport Control Sign`。
- 新增單字：`passport control`、`visa`、`stamp`；文章融入複習字：`hall`、`wrong`、`number`。
- 補齊 `article.mp3` 與 `s01.mp3` 到 `s20.mp3`，並同步首頁、`profile.json`、`vocabulary/learning.json`、`.ai/PROJECT_STATE.md`。
- 驗證：句子編號連續、20 個單句音檔存在、Review Quiz 36 題、首頁條目存在、本機 HTTP 200。

## 2026-06-15 — Day 58 今日英文練習產出

- 先 `git fetch --all --prune` / `git pull --ff-only` 同步遠端 `vocabulary/learning.json`，確保 review 區塊使用最新 SRS。
- 依 `profile.json.lastTopic = travel` 產出 `daily` 主題，新增 `daily/2026-06-15/`，標題為 `Reading a Cafe Wi-Fi Sign`。
- 新增單字：`Wi-Fi code`、`outlet`、`refill`；文章融入複習字：`busy`、`message`、`card`。
- 補齊 `article.mp3` 與 `s01.mp3` 到 `s18.mp3`，並同步首頁、`profile.json`、`vocabulary/learning.json`、`.ai/PROJECT_STATE.md`。
- 驗證：句子編號連續、18 個單句音檔存在、Review Quiz 24 題、首頁條目存在、本機 HTTP 200。

## 2026-06-16 — Day 59 連載小說模式啟動

- 先 `git fetch --all --prune` / `git pull --ff-only` 同步遠端 `vocabulary/learning.json`，確保 review 區塊使用最新 SRS。
- 建立 `.ai/serial-story/` 文件：`SERIES_BIBLE.md`、`SEASON_1_OUTLINE.md`、`STYLE_GUIDE.md`、`CONTINUITY_LOG.md`。
- 更新 `AGENTS.md`、`.ai/daily-english-learning/SKILL.md`、`.ai/DECISIONS.md`，將每日文章主體改為連載小說模式，下方練習與 SRS 複習維持原樣。
- 新增 `daily/2026-06-16/`，標題為 `The Blue Receipt · Episode 1`。
- 新增單字：`bottom`、`printed`、`warning`；文章融入複習字：`window`、`Wi-Fi code`、`outlet`、`refill`。
- 補齊 `article.mp3` 與 `s01.mp3` 到 `s18.mp3`，並同步首頁、`profile.json`、`vocabulary/learning.json`、`.ai/PROJECT_STATE.md`、`.ai/serial-story/CONTINUITY_LOG.md`。
- 驗證：句子編號連續、18 個單句音檔存在、Review Quiz 3 題、首頁條目存在、本機 HTTP 200。

## 2026-06-22 — Day 61 正式教材產出

- 先 `git fetch --all --prune` / `git pull --ff-only` 同步遠端 `vocabulary/learning.json`，避免用過期 SRS 生成 review。
- 延續 serial story continuity，新增 `daily/2026-06-22/`，標題為 `The Blue Receipt · Episode 3`。
- 今日新字：`front`、`saved`、`ride`；文章融入複習字：`warning`、`nearby`、`block`。
- Review Quiz / Review Words 依最新 `learning.json` 生成，共納入 50 個到期複習字。
- Speaking Bridge 使用 `block`、`listed`、`nearby`、`warning`。
- 補齊 `article.mp3` 與 `s01.mp3` 到 `s20.mp3`，並同步首頁、`profile.json`、`vocabulary/learning.json`、`.ai/PROJECT_STATE.md`、`.ai/serial-story/CONTINUITY_LOG.md`。
- 驗證：句子編號連續、20 個單句音檔存在、本機 HTTP 200。

## 2026-06-23 — Day 62 正式教材產出

- 先同步遠端 SRS；同步過程中第一次 `git fetch` 出現 remote ref 鎖衝突，但後續 `git pull --ff-only` 已成功更新到最新 `vocabulary/learning.json`。
- 延續 serial story continuity，新增 `daily/2026-06-23/`，標題為 `The Blue Receipt · Episode 4`。
- 今日新字：`search`、`post`、`title`；文章融入複習字：`front`、`saved`、`ride`。
- Review Quiz / Review Words 依最新 `learning.json` 生成，共納入 4 個到期複習字。
- Speaking Bridge 使用 `listed`、`block`、`nearby`、`warning`。
- 補齊 `article.mp3` 與 `s01.mp3` 到 `s22.mp3`，並同步首頁、`profile.json`、`vocabulary/learning.json`、`.ai/PROJECT_STATE.md`、`.ai/serial-story/CONTINUITY_LOG.md`。
- 驗證：句子編號連續、22 個單句音檔存在、本機 HTTP 200。

## 2026-06-24 — Day 63 正式教材產出

- 先同步遠端 SRS；同步後以最新 `vocabulary/learning.json` 重算 review，今天共 3 個到期複習字。
- 延續 serial story continuity，新增 `daily/2026-06-24/`，標題為 `The Blue Receipt · Episode 5`。
- 今日新字：`arrow`、`poster`、`photo`；文章融入複習字：`search`、`post`、`title`。
- Speaking Bridge 使用 `front`、`ride`、`saved`、`listed`。
- 補齊 `article.mp3` 與 `s01.mp3` 到 `s21.mp3`，並同步首頁、`profile.json`、`vocabulary/learning.json`、`.ai/PROJECT_STATE.md`、`.ai/serial-story/CONTINUITY_LOG.md`。
- 驗證：句子編號連續、21 個單句音檔存在、本機 HTTP 200。

## 2026-06-25 — Day 64 正式教材產出

- 先同步遠端 SRS；第一次 `pull` 因 repo 設定失敗，改用 `git merge --ff-only FETCH_HEAD` 補到最新遠端狀態。
- 依最新 `vocabulary/learning.json` 重算 review，今天共 9 個到期複習字。
- 延續 serial story continuity，新增 `daily/2026-06-25/`，標題為 `The Blue Receipt · Episode 6`。
- 今日新字：`locked`、`hallway`、`basement`；文章融入複習字：`arrow`、`poster`、`photo`。
- Speaking Bridge 使用 `post`、`search`、`title`、`front`。
- 補齊 `article.mp3` 與 `s01.mp3` 到 `s21.mp3`，並同步首頁、`profile.json`、`vocabulary/learning.json`、`.ai/PROJECT_STATE.md`、`.ai/serial-story/CONTINUITY_LOG.md`。
- 驗證：句子編號連續、21 個單句音檔存在、本機 HTTP 200。

## 2026-06-26 — Day 65 正式教材產出

- 先以遠端最新 SRS commit 為底，再合併今天新增單字重算 review，今天共 32 個到期複習字，且無逾期字。
- 延續 serial story continuity，新增 `daily/2026-06-26/`，標題為 `The Blue Receipt · Episode 7`。
- 今日新字：`storage`、`folder`、`record`；文章融入複習字：`locked`、`hallway`、`basement`。
- Speaking Bridge 使用 `arrow`、`photo`、`poster`、`post`。
- 補齊 `article.mp3` 與 `s01.mp3` 到 `s22.mp3`，並同步首頁、`profile.json`、`vocabulary/learning.json`、`.ai/PROJECT_STATE.md`、`.ai/serial-story/CONTINUITY_LOG.md`。
- 驗證：句子編號連續、22 個單句音檔存在、本機 HTTP 200。
