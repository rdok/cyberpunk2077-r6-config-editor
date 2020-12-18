$ScriptDir = Split-Path $script:MyInvocation.MyCommand.Path
. ${ScriptDir}\setup-venv.ps1

Set-Location ${ScriptDir}\..

pyinstaller --onefile src\main.py