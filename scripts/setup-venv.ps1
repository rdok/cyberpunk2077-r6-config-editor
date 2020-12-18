param (
    [Parameter(Mandatory = $true)][string]$env
)

If ($env -ne 'prod' -And $env -ne 'dev')
{
    throw "Invalid env. Should be dev or prod."
}

$ScriptDir = Split-Path $script:MyInvocation.MyCommand.Path
$RootDir = "${ScriptDir}\.."
Set-Location ${RootDir}

python -m venv .venv

. ${RootDir}\.venv\Scripts\Activate.ps1

If ($env -eq 'prod')
{
    pip install -r requirements.prod.lock
} else {
    pip install -r requirements.prod.lock -r requirements.dev.lock
}
