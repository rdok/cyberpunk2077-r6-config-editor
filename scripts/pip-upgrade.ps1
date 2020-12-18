$ScriptDir = Split-Path $script:MyInvocation.MyCommand.Path
. ${ScriptDir}\setup-venv.ps1

$RootDir = "${ScriptDir}\.."

. ${RootDir}\.venv\Scripts\python.exe -m pip install --upgrade pip

