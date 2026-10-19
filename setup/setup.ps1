# Windows setup for the hyperank video studio. PowerShell 5.1 compatible, safe to re-run.
#
#   powershell -ExecutionPolicy Bypass -File setup\setup.ps1          # asks before each winget install
#   powershell -ExecutionPolicy Bypass -File setup\setup.ps1 -Yes     # installs missing tools without asking
#
# Every step prints what it is doing and skips itself when the work is already done.

param([switch]$Yes)

$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'   # Invoke-WebRequest is far faster without the progress bar
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

$Repo = Split-Path -Parent $PSScriptRoot
$HyperframesVersion = '0.8.113'            # pinned on purpose so films re-render identically; never bump it here
$WhisperTag = 'b5130'
$WhisperZip = "https://github.com/ggml-org/whisper.cpp/releases/download/$WhisperTag/whisper-bin-x64.zip"
$WhisperModelUrl = 'https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-small.en.bin'
$KokoroBase = 'https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0'

$WhisperDir = Join-Path $HOME 'tools\whisper.cpp'
$HfCache = Join-Path $HOME '.cache\hyperframes'
$WhisperModel = Join-Path $HfCache 'whisper\models\ggml-small.en.bin'
$KokoroModel = Join-Path $HfCache 'tts\models\kokoro-v1.0.onnx'
$KokoroVoices = Join-Path $HfCache 'tts\voices\voices-v1.0.bin'

function Step($n, $text) { Write-Host ''; Write-Host "[$n] $text" -ForegroundColor Cyan }
function Info($text) { Write-Host "    $text" }

function Refresh-Path {
    $machine = [Environment]::GetEnvironmentVariable('Path', 'Machine')
    $user = [Environment]::GetEnvironmentVariable('Path', 'User')
    $env:Path = "$machine;$user"
}

function Has-Command($name) { return [bool](Get-Command $name -ErrorAction SilentlyContinue) }

function Has-RealPython {
    # the Microsoft Store "python" alias exists on a clean Windows and prints nothing useful, so run it
    if (-not (Has-Command 'python')) { return $false }
    try { $v = & python --version 2>&1; return ($LASTEXITCODE -eq 0 -and "$v" -match 'Python 3\.') } catch { return $false }
}

function Ensure-Tool($label, $isPresent, $wingetId) {
    if (& $isPresent) { Info "$label already installed"; return }
    if (-not (Has-Command 'winget')) {
        Write-Warning "$label is missing and winget is not available. Install $label by hand, then re-run this script."
        return
    }
    $go = $Yes
    if (-not $go) { $go = ((Read-Host "    $label is missing. Install it with winget ($wingetId)? [Y/n]") -notmatch '^[nN]') }
    if (-not $go) { Write-Warning "Skipped $label. The studio will not fully work without it."; return }
    & winget install --id $wingetId -e --accept-package-agreements --accept-source-agreements
    Refresh-Path
    if (-not (& $isPresent)) { Write-Warning "$label installed but is not on PATH yet. Open a new terminal and re-run this script." }
}

function Download($url, $dest) {
    if (Test-Path $dest) { Info "already there: $dest"; return }
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $dest) | Out-Null
    $part = "$dest.part"
    Info "downloading $url"
    Invoke-WebRequest -Uri $url -OutFile $part -UseBasicParsing
    Move-Item -Force $part $dest
    Info "saved $dest"
}

function Tree-Hash($dir) {
    # one string describing a folder's contents, to tell a changed skill from an identical one
    $root = (Resolve-Path $dir).Path
    $lines = Get-ChildItem -Recurse -File $dir | Sort-Object FullName | ForEach-Object {
        $_.FullName.Substring($root.Length) + ':' + (Get-FileHash -Algorithm SHA1 $_.FullName).Hash
    }
    return ($lines -join "`n")
}

# ---------------------------------------------------------------- 1
Step 1 'Core tools: Git, Node.js LTS, Python 3.13, ffmpeg'
Ensure-Tool 'Git' { Has-Command 'git' } 'Git.Git'
Ensure-Tool 'Node.js LTS' { (Has-Command 'node') -and (Has-Command 'npx') } 'OpenJS.NodeJS.LTS'
Ensure-Tool 'Python 3.13' { Has-RealPython } 'Python.Python.3.13'
Ensure-Tool 'ffmpeg' { (Has-Command 'ffmpeg') -and (Has-Command 'ffprobe') } 'Gyan.FFmpeg'

# ---------------------------------------------------------------- 2
Step 2 'Python packages (the imports of tts.py, build.py, appkit.py, sfx.py, mark.py, tts_batch.py and the capture scripts)'
if (Has-RealPython) {
    # kokoro-onnx + soundfile: local Kokoro TTS; numpy + soundfile: sfx.py and tts.py; beautifulsoup4: appkit.py and the tutorial build;
    # pillow: capture/mark.py; playwright: capture scripts. Nothing is version-pinned because no versions were verified.
    & python -m pip install --user --upgrade kokoro-onnx soundfile numpy beautifulsoup4 pillow playwright
    if ($LASTEXITCODE -ne 0) { throw 'pip install failed' }
    Info 'installing the Playwright Chromium used by the intro and tutorial capture scripts'
    & python -m playwright install chromium
    if ($LASTEXITCODE -ne 0) { Write-Warning 'playwright chromium install failed; only the capture scripts need it, builds and renders do not' }
} else {
    Write-Warning 'Python is not available yet, skipping pip. Re-run this script from a new terminal.'
}

# ---------------------------------------------------------------- 3
Step 3 "whisper.cpp $WhisperTag and the small.en model"
if (Test-Path (Join-Path $WhisperDir 'Release\whisper-cli.exe')) {
    Info 'whisper-cli.exe already installed'
} else {
    $zip = Join-Path $env:TEMP 'whisper-bin-x64.zip'
    Download $WhisperZip $zip
    New-Item -ItemType Directory -Force -Path $WhisperDir | Out-Null
    Expand-Archive -Path $zip -DestinationPath $WhisperDir -Force   # the zip holds a Release\ folder
    Remove-Item $zip -Force
    Info "extracted to $WhisperDir"
}
# Invoke-WebRequest here, not the hyperframes CLI: its own 30 s download timeout fails on this 488 MB file
Download $WhisperModelUrl $WhisperModel

# ---------------------------------------------------------------- 4
Step 4 'Claude Code skills into ~/.claude/skills (existing folders are backed up first)'
$SkillsSrc = Join-Path $Repo 'skills'
$SkillsDst = Join-Path $HOME '.claude\skills'
$stamp = Get-Date -Format 'yyyyMMdd-HHmmss'
$Backup = Join-Path $HOME ".claude\_backups\skills-$stamp"
New-Item -ItemType Directory -Force -Path $SkillsDst | Out-Null
foreach ($s in Get-ChildItem -Directory $SkillsSrc) {
    $target = Join-Path $SkillsDst $s.Name
    if (Test-Path $target) {
        if ((Tree-Hash $s.FullName) -eq (Tree-Hash $target)) { Info "$($s.Name): identical, left alone"; continue }
        New-Item -ItemType Directory -Force -Path $Backup | Out-Null
        Move-Item $target (Join-Path $Backup $s.Name)
        Info "$($s.Name): old copy moved to $Backup"
    }
    Copy-Item -Recurse $s.FullName $target
    Info "$($s.Name): installed"
}

# ---------------------------------------------------------------- 5
Step 5 "Warm the pinned HyperFrames CLI ($HyperframesVersion)"
if (Has-Command 'npx') {
    & npx.cmd --yes "hyperframes@$HyperframesVersion" --version
    if ($LASTEXITCODE -ne 0) { Write-Warning 'hyperframes CLI did not start; check your network and Node install' }
} else {
    Write-Warning 'npx is not available yet, skipping. Re-run this script from a new terminal.'
}

# ---------------------------------------------------------------- 6
Step 6 'Kokoro TTS model files'
# HyperFrames and the templates' tts.py / tts_batch.py read these exact paths under ~/.cache/hyperframes/tts
Download "$KokoroBase/kokoro-v1.0.onnx" $KokoroModel
Download "$KokoroBase/voices-v1.0.bin" $KokoroVoices

Write-Host ''
Write-Host 'Setup finished.' -ForegroundColor Green
Write-Host 'The first render or check also downloads HyperFrames own Chrome into ~/.cache/hyperframes/chrome; that is expected.'
Write-Host 'Next: open this folder in Claude Code and read CLAUDE.md and README.md.'
