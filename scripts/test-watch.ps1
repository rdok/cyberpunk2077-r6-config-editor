$ScriptDir = Split-Path $script:MyInvocation.MyCommand.Path
$RootDir = "${ScriptDir}/.."

Write-Output "Output some message"

$testWatch = "cd ${RootDir}; " `
    + "python -m venv .venv; " `
    + "pip install -r requirements.lock; " `
    + ". ${RootDir}\.venv\Scripts\Activate.ps1; " `
    + "pytest-watch"

Invoke-Expression $testWatch