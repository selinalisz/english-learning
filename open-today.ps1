param(
    [int]$Port = 8080
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$dailyDir = Join-Path $repoRoot "daily"

# Stop process listening on the target port (if any).
try {
    $connections = Get-NetTCPConnection -LocalPort $Port -State Listen -ErrorAction Stop
    $pids = $connections | Select-Object -ExpandProperty OwningProcess -Unique
    foreach ($pid in $pids) {
        if ($pid -and $pid -ne 0) {
            Stop-Process -Id $pid -Force -ErrorAction SilentlyContinue
        }
    }
} catch {
    # Ignore when command is unavailable or no listener exists.
}

# Locate python command.
$pythonCmd = $null
if (Test-Path "C:\Python314\python.exe") {
    $pythonCmd = "C:\Python314\python.exe"
} elseif (Get-Command py -ErrorAction SilentlyContinue) {
    $pythonCmd = "py"
} elseif (Get-Command python -ErrorAction SilentlyContinue) {
    $pythonCmd = "python"
}

if (-not $pythonCmd) {
    Write-Host "Python not found. Please install Python first." -ForegroundColor Red
    exit 1
}

$serverScript = Join-Path $repoRoot "local_server.py"
if (-not (Test-Path $serverScript)) {
    Write-Host "local_server.py not found: $serverScript" -ForegroundColor Red
    exit 1
}

$pythonArgs = if ($pythonCmd -eq "py") {
    "-3 `"$serverScript`" --port $Port --root `"$repoRoot`""
} else {
    "`"$serverScript`" --port $Port --root `"$repoRoot`""
}

Start-Process -FilePath $pythonCmd -ArgumentList $pythonArgs -WorkingDirectory $repoRoot -WindowStyle Minimized
Start-Sleep -Milliseconds 900

$url = "http://localhost:$Port/index.html"
Start-Process $url

Write-Host "Opened: $url" -ForegroundColor Green
