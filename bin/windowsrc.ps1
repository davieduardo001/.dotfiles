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
if ($wslInstalled.State -ne "Enabled") {
    Write-Color "Installing WSL and Ubuntu..." $YELLOW
    wsl --install -d Ubuntu
} else {
    Write-Color "WSL is already installed" $GREEN
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

# Install Firefox using Chocolatey
Write-Color "Installing Firefox..." $YELLOW
if (-not (Get-Command "firefox" -ErrorAction SilentlyContinue)) {
    choco install firefox -y
} else {
    Write-Color "Firefox is already installed" $GREEN
}

# Install Visual Studio Code using Chocolatey
Write-Color "Installing Visual Studio Code..." $YELLOW
if (-not (Get-Command "code" -ErrorAction SilentlyContinue)) {
    choco install vscode -y
} else {
    Write-Color "Visual Studio Code is already installed" $GREEN
}

# Install FiraCode font
Write-Color "Installing FiraCode font..." $YELLOW
$fontUrl = "https://github.com/ryanoasis/nerd-fonts/releases/download/v3.2.1/FiraCode.zip"
$fontZip = "$env:TEMP\FiraCode.zip"
$fontExtractPath = "$env:TEMP\FiraCode"

# Download and extract the font
Invoke-WebRequest -Uri $fontUrl -OutFile $fontZip
Expand-Archive -Path $fontZip -DestinationPath $fontExtractPath

# Install the font
$fontFiles = Get-ChildItem -Path "$fontExtractPath\FiraCode" -Filter "*.ttf"
foreach ($file in $fontFiles) {
    $fontName = [System.IO.Path]::GetFileNameWithoutExtension($file.FullName)
    Write-Color "Installing $fontName..." $YELLOW
    $fontDestination = "$env:SystemRoot\Fonts\$fontName.ttf"
    Copy-Item -Path $file.FullName -Destination $fontDestination -Force
    Write-Color "$fontName installed" $GREEN
}

# Clean up extracted files
Remove-Item -Path $fontZip -Force
Remove-Item -Path $fontExtractPath -Recurse -Force

Write-Color "Installation completed." $GREEN
