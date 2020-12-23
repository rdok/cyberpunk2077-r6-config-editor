$ScriptDir = Split-Path $script:MyInvocation.MyCommand.Path
. ${ScriptDir}\setup-venv.ps1 -env prod

Set-Location ${ScriptDir}\..

If ($env -eq 'prod')
{
    pyinstaller --onefile src\main.py --name cyberpunk2077-r6-config-editor --windowed --icon=logo.ico
} else {
    pyinstaller --onefile src\main.py --name cyberpunk2077-r6-config-editor --icon=logo.ico --console
}

