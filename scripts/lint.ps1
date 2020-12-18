$ScriptDir = Split-Path $script:MyInvocation.MyCommand.Path
$RootDir = "${ScriptDir}/.."

$testWatch = "cd ${RootDir}; " `
    + "python -m venv .venv; " `
    + "pip install -r requirements.lock; " `
    + ". ${RootDir}\.venv\Scripts\Activate.ps1; " `
    + "flake8 src"

Invoke-Expression $testWatch