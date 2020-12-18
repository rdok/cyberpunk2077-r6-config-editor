param (
    [Parameter(Mandatory = $true)][string]$package,
    [Parameter(Mandatory = $true)][string]$env
)

If ($env -ne 'prod' -And $env -ne 'dev')
{
    throw "Invalid env. Should be dev or prod."
}

$ScriptDir = Split-Path $script:MyInvocation.MyCommand.Path
. ${ScriptDir}\setup-venv.ps1 -env $env

pip install ${package}

pip freeze | Select-String -Pattern ${package}= | Add-Content requirements.${env}.lock
