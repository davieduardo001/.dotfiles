# PowerShell script to set up Windows with WSL2, Ubuntu, PowerShell, Chocolatey, Visual Studio Code, Code - OSS, and Oh-My-Posh

$RED = "Red"
$GREEN = "Green"
$YELLOW = "Yellow"
$MAGENTA = "Magenta"

# Helper function to write colored messages
function Write-Color {
    param (
        [string]$Message,
        [string]$Color
    )
    Write-Host $Message -ForegroundColor $Color
}

Write-Color "Starting installation..." $YELLOW

# Check for administrative privileges
if (-not ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    Write-Color "You need to run this script as an Administrator." $RED
    exit
}

# Check if WSL is installed
Write-Color "Checking if WSL is installed..." $YELLOW
$wslInstalled = Get-WindowsOptionalFeature -Online | Where-Object { $_.FeatureName -eq "Microsoft-Windows-Subsystem-Linux" }
if ($wslInstalled.State -eq "Enabled") {
    Write-Color "WSL is already installed" $GREEN
} else {
    Write-Color "Installing WSL and Ubuntu..." $YELLOW
    wsl --install -d Ubuntu
}

# Install PowerShell
Write-Color "Installing PowerShell..." $YELLOW
if (-not (Get-Command "pwsh" -ErrorAction SilentlyContinue)) {
    # Download and install PowerShell
    $powershellUrl = "https://github.com/PowerShell/PowerShell/releases/download/v7.3.0/PowerShell-7.3.0-win-x64.msi"
    $installerPath = "$env:TEMP\PowerShell-7.3.0-win-x64.msi"
    Invoke-WebRequest -Uri $powershellUrl -OutFile $installerPath
    Start-Process msiexec.exe -ArgumentList "/i", $installerPath, "/quiet", "/norestart" -NoNewWindow -Wait
    Remove-Item -Path $installerPath
} else {
    Write-Color "PowerShell is already installed" $GREEN
}

# Install Chocolatey
Write-Color "Installing Chocolatey..." $YELLOW
if (-not (Get-Command "choco" -ErrorAction SilentlyContinue)) {
    Set-ExecutionPolicy Bypass -Scope Process -Force
    [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
    iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
} else {
    Write-Color "Chocolatey is already installed" $GREEN
}

# Install Code - OSS using winget
Write-Color "Installing Code - OSS using winget..." $YELLOW
if (-not (Get-Command "code-oss" -ErrorAction SilentlyContinue)) {
    winget install --id Microsoft.CodeOSS -e
} else {
    Write-Color "Code - OSS is already installed" $GREEN
}
