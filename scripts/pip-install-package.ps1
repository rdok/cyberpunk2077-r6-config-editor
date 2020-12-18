param ([Parameter(Mandatory=$true)][string]$package)
# Usage: .\scripts\pip-install-package.ps1 -package packagename

$ScriptDir = Split-Path $script:MyInvocation.MyCommand.Path
. ${ScriptDir}\setup-venv.ps1

pip install ${package}

pip freeze | Select-String -Pattern ${package}= | Add-Content requirements.lock
