# English Learning App

## What Changed

This app is no longer just a static site served by `http.server`.

- The homepage has a `生成今日页面+音频` button.
- That button calls the local API endpoint `POST /__generate_today`.
- The API is provided by `local_server.py`.
- Newly generated daily pages include:
  - article audio + sentence audio
  - playback speed buttons
  - saved speed preference via `localStorage`
  - a back-to-home button

Because of that, if you want the generate button to work, you must start `local_server.py` instead of a plain static file server.

## Quick Start (macOS)

1. Open Terminal and go to this project folder.
2. Start the local generation server:

```bash
python3 local_server.py --port 8080 --root .
```

3. Open your browser:

```text
http://localhost:8080
```

4. Click `生成今日页面+音频` on the homepage if you want to create today's page and audio.

5. Open the latest daily page (example):

```text
http://localhost:8080/daily/2026-07-06/
```

## Quick Start (Windows)

1. Open PowerShell and go to this project folder.
2. Start the local generation server:

```powershell
python local_server.py --port 8080 --root .
```

3. Open your browser:

```text
http://localhost:8080
```

4. Click `生成今日页面+音频` on the homepage if you want to create today's page and audio.

5. Open the latest daily page (example):

```text
http://localhost:8080/daily/2026-07-06/
```

## Requirements

- Python 3
- `edge-tts` for audio generation

Example install:

```bash
pip install edge-tts
```

If you only start `python -m http.server`, old static pages can still open, but the homepage generate button will not work because `/__generate_today` does not exist there.

## One-Click Start Scripts

### macOS

Run:

```bash
./open-today.command
```

If permission is denied:

```bash
chmod +x open-today.command
./open-today.command
```

- This script now starts `local_server.py`, not `http.server`.
- It uses repo-relative paths, so it can be moved to another Mac without editing hard-coded paths.
- It opens the homepage so you can click `生成今日页面+音频`.
- After generation, use the homepage's today link or the daily page list to open the created lesson.

### Windows

Run:

```powershell
.\open-today.ps1
```

Or double-click:

```text
open-today.cmd
```

- This script starts `local_server.py` and opens today's page automatically.
- This script starts `local_server.py` and opens the homepage first.
- From the homepage, click `生成今日页面+音频`, then open the generated lesson.

## Homepage Generate Button

The homepage button:

- generates today's HTML page
- generates `article.mp3`
- generates sentence audio `s01.mp3` to `sNN.mp3`
- updates learning/profile data used by the local workflow

If generation fails, first make sure you launched the site with:

- macOS: `open-today.command`
- Windows: `open-today.ps1`

## Daily Page Features

Generated daily pages now include:

- article audio player
- sentence-by-sentence playback
- speed buttons: `超慢速 / 慢速 / 中速 / 快速`
- remembered speed preference via `localStorage`
- `返回首页` button

## SRS Local Save (No GitHub Required)

This app can save SRS progress locally.

1. Open the daily page.
2. In Active Recall section, click:
   - Bind local learning.json (auto write)
3. Select your local JSON file, for example [vocabulary/learning.json](vocabulary/learning.json).
4. Submit quiz answers. SRS will be written back to that local file automatically.

Notes:
- First-time bind is required by browser security.
- Best support: latest Chrome/Edge.
- Safari may not support direct local file write.

## Optional Manual URLs

Homepage:

```text
http://localhost:8080
```

Example daily page:

```text
http://localhost:8080/daily/2026-07-06/
```
