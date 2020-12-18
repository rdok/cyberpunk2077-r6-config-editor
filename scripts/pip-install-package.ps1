param ([Parameter(Mandatory=$true)][string]$package)

# Usage: ./scripts/pip-install-package.ps1 -package packagename

$ScriptDir = Split-Path $script:MyInvocation.MyCommand.Path
$RootDir = "${ScriptDir}/.."

$pipInstallPackage = "cd ${RootDir}; " `
    + "pip install ${package}; " `

Invoke-Expression $pipInstallPackage

pip freeze | Select-String -Pattern ${package}= | Add-Content requirements.lock
