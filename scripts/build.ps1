$ScriptDir = Split-Path $script:MyInvocation.MyCommand.Path
. ${ScriptDir}\setup-venv.ps1 -env prod

Set-Location ${ScriptDir}\..

pyinstaller --onefile src\main.py --name cyberpunk2077-usability