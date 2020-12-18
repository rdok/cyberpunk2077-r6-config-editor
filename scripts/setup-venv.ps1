$ScriptDir = Split-Path $script:MyInvocation.MyCommand.Path
$RootDir = "${ScriptDir}\.."
Set-Location ${RootDir}

python3 -m venv .venv

. ${RootDir}\.venv\Scripts\Activate.ps1

pip install -r requirements.lock
