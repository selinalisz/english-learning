param(
    [int]$Port = 8080
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$dailyDir = Join-Path $repoRoot "daily"

if (-not (Test-Path $dailyDir)) {
    Write-Host "daily folder not found: $dailyDir" -ForegroundColor Red
    exit 1
}

# Find date folders with index.html, newest first.
$dateItems = Get-ChildItem -Path $dailyDir -Directory |
    Where-Object { $_.Name -match '^\d{4}-\d{2}-\d{2}$' -and (Test-Path (Join-Path $_.FullName 'index.html')) } |
    Sort-Object Name -Descending

if (-not $dateItems -or $dateItems.Count -eq 0) {
    Write-Host "No learning pages found under daily/." -ForegroundColor Yellow
    exit 1
}

$today = Get-Date -Format "yyyy-MM-dd"
$targetDate = if ($dateItems.Name -contains $today) { $today } else { $dateItems[0].Name }

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

$pythonArgs = if ($pythonCmd -eq "py") {
    "-3 -m http.server $Port --directory `"$repoRoot`""
} else {
    "-m http.server $Port --directory `"$repoRoot`""
}

Start-Process -FilePath $pythonCmd -ArgumentList $pythonArgs -WorkingDirectory $repoRoot -WindowStyle Minimized
Start-Sleep -Milliseconds 900

$url = "http://localhost:$Port/daily/$targetDate/"
Start-Process $url

Write-Host "Opened: $url" -ForegroundColor Green
