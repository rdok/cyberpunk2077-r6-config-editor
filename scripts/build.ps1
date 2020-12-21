param (
    [Parameter(Mandatory = $true)][string]$env
)

If ($env -ne 'prod' -And $env -ne 'dev')
{
    throw "Invalid env. Should be dev or prod."
}

$ScriptDir = Split-Path $script:MyInvocation.MyCommand.Path
. ${ScriptDir}\setup-venv.ps1 -env prod

Set-Location ${ScriptDir}\..

If ($env -eq 'prod')
{
    pyinstaller --onefile src\main.py --name cyberpunk2077-usability --windowed
} else {
    pyinstaller --onefile src\main.py --name cyberpunk2077-usability --debug
}
