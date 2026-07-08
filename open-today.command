#!/bin/sh
set -eu

PORT="${PORT:-8080}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$SCRIPT_DIR"
DAILY_DIR="$REPO_ROOT/daily"
SERVER_SCRIPT="$REPO_ROOT/local_server.py"
LOG_FILE="${TMPDIR:-/tmp}/daily-english-server.log"

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

if command -v lsof >/dev/null 2>&1; then
  PIDS="$(lsof -ti tcp:"$PORT" 2>/dev/null || true)"
  if [ -n "$PIDS" ]; then
    echo "$PIDS" | xargs kill -9 >/dev/null 2>&1 || true
  fi
fi

cd "$REPO_ROOT"
nohup "$PYTHON_CMD" "$SERVER_SCRIPT" --port "$PORT" --root "$REPO_ROOT" >"$LOG_FILE" 2>&1 &

HOME_URL="http://localhost:$PORT/index.html"

if command -v curl >/dev/null 2>&1; then
  i=0
  while [ "$i" -lt 30 ]; do
    if curl -fsS "http://127.0.0.1:$PORT/" >/dev/null 2>&1; then
      break
    fi
    i=$((i + 1))
    sleep 0.2
  done
else
  sleep 1
fi

open "$HOME_URL"
