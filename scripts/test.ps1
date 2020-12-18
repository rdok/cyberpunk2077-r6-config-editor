$ScriptDir = Split-Path $script:MyInvocation.MyCommand.Path
$RootDir = "${ScriptDir}/.."

$testWatch = "cd ${RootDir}; " `
    + "python3 -m venv .venv; " `
    + "pip3 install -r requirements.lock; " `
    + ". ${RootDir}\.venv\Scripts\Activate.ps1; " `
    + "pytest"

Invoke-Expression $testWatch