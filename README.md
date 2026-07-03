# English Learning App

## Quick Start (macOS)

1. Open Terminal and go to this project folder.
2. Start a local server:

```bash
python3 -m http.server 8000
```

3. Open your browser:

```text
http://localhost:8000
```

4. Open the latest daily page (example):

```text
http://localhost:8000/daily/2026-07-03/
```

## Quick Start (Windows)

1. Open PowerShell and go to this project folder.
2. Start a local server:

```powershell
python -m http.server 8000
```

3. Open your browser:

```text
http://localhost:8000
```

4. Open the latest daily page (example):

```text
http://localhost:8000/daily/2026-07-03/
```

## SRS Local Save (No GitHub Required)

This app can save SRS progress locally.

1. Open the daily page.
2. In Active Recall section, click:
   - Bind local learning.json (auto write)
3. Select your local JSON file (for example `learning.json` in this repo).
4. Submit quiz answers. SRS will be written back to that local file automatically.

Notes:
- First-time bind is required by browser security.
- Best support: latest Chrome/Edge.
- Safari may not support direct local file write.

## Optional Script

If you want one-click start on macOS, you can also run:

```bash
./open-today.command
```

If permission is denied:

```bash
chmod +x open-today.command
./open-today.command
```

If you want one-click start on Windows, you can also run:

```powershell
.\open-today.ps1
```

Or double-click:

```text
open-today.cmd
```
