#!/bin/bash
set -euo pipefail

PORT="${PORT:-8080}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$SCRIPT_DIR"
DAILY_DIR="$REPO_ROOT/daily"
SERVER_SCRIPT="$REPO_ROOT/local_server.py"

if [ ! -f "$SERVER_SCRIPT" ]; then
  osascript -e 'display alert "找不到 local_server.py" message "請確認專案完整後再啟動" as warning'
  exit 1
fi

if [ -x "$REPO_ROOT/.venv/bin/python" ]; then
  PYTHON_CMD="$REPO_ROOT/.venv/bin/python"
elif command -v python3 >/dev/null 2>&1; then
  PYTHON_CMD="python3"
elif command -v python >/dev/null 2>&1; then
  PYTHON_CMD="python"
else
  osascript -e 'display alert "找不到 Python" message "請先安裝 Python 3" as warning'
  exit 1
fi

# 若目標 port 已在跑，先關掉舊服務。
if lsof -ti tcp:"$PORT" >/dev/null 2>&1; then
  lsof -ti tcp:"$PORT" | xargs kill -9 2>/dev/null || true
fi

cd "$REPO_ROOT"
nohup "$PYTHON_CMD" "$SERVER_SCRIPT" --port "$PORT" --root "$REPO_ROOT" >/tmp/daily-english-server.log 2>&1 &
sleep 0.9

# 取出可開啟的日期列表（由新到舊）。
DATES_RAW=""
if [ -d "$DAILY_DIR" ]; then
  DATES_RAW=$(ls -1 "$DAILY_DIR" 2>/dev/null \
    | grep -E '^[0-9]{4}-[0-9]{2}-[0-9]{2}$' \
    | sort -r \
    | while read -r d; do
        [ -f "$DAILY_DIR/$d/index.html" ] && echo "$d"
      done)
fi

# 若尚無任何日期頁，直接進首頁（可用「生成今日页面+音频」）。
if [ -z "$DATES_RAW" ]; then
  open "http://localhost:$PORT/index.html"
  exit 0
fi

TODAY=$(date +%Y-%m-%d)
DATES_LABELED=$(echo "$DATES_RAW" | awk -v today="$TODAY" '
  NR==1 && $0==today { print $0 " （今天）"; next }
  { print }
')
DATES_AS=$(echo "$DATES_LABELED" | awk '{printf "\"%s\", ", $0}' | sed 's/, $//')

SELECTED=$(osascript <<EOF
set dateList to {$DATES_AS}
set chosen to choose from list dateList ¬
  with prompt "選擇要開啟哪一天的學習內容：" ¬
  default items {item 1 of dateList} ¬
  with title "📖 Daily English"
if chosen is false then return ""
return item 1 of chosen
EOF
)

[ -z "$SELECTED" ] && exit 0
DATE_KEY=$(echo "$SELECTED" | grep -oE '[0-9]{4}-[0-9]{2}-[0-9]{2}')
open "http://localhost:$PORT/daily/$DATE_KEY/"
