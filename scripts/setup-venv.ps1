$ScriptDir = Split-Path $script:MyInvocation.MyCommand.Path
$RootDir = "${ScriptDir}\.."
Set-Location ${RootDir}

python -m venv .venv

. ${RootDir}\.venv\Scripts\Activate.ps1

pip install -r requirements.lock
