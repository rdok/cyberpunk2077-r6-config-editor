$ScriptDir = Split-Path $script:MyInvocation.MyCommand.Path
$RootDir = "${ScriptDir}/.."
Set-Location ${RootDir}

python -m venv .venv

pip install -r requirements.lock

. ${RootDir}\.venv\Scripts\Activate.ps1;