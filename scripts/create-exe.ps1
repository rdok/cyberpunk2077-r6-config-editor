$ScriptDir = Split-Path $script:MyInvocation.MyCommand.Path
. ${ScriptDir}\setup-venv.ps1

$RootDir = "${ScriptDir}\.."

Set-Location $RootDir

pyinstaller --onefile ${RootDir}\src\main.py