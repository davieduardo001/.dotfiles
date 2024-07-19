import os
import subprocess
from utils.colors import colors

DOTFILES_DIR = '~/.dotfiles'

# check SDKMAN!
def is_sdkman_installed():
    # Check if the 'sdk' executable is in the PATH
    sdkman_dir = os.path.expanduser('~/.sdkman')
    return os.path.exists(sdkman_dir) and os.path.isdir(sdkman_dir)

# install SDKMAN!
def install_sdkman():
    # Install SDKMAN! using the provided installation command for Arch Linux
    if is_sdkman_installed():
        print(f'{colors.GREEN}* SDKMAN! is already installed.{colors.RESET}\n')
    else:
        print(f'{colors.RED}* SDKMAN! is not installed. Installing...{colors.RESET}\n')
        install_cmd = 'curl -s "https://get.sdkman.io" | bash'
        os.system(install_cmd)
        print()

# check git
def is_git_installed():
    try:
        result = subprocess.run(['git', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True # Check if the return code is 0, indicating success
    except subprocess.CalledProcessError:
        return False  # Handle the case where Git command fails

# install git
def install_git(iso):
    if is_git_installed():
        print(f'{colors.GREEN}* git is already installed.{colors.RESET}\n')
    else:
        print(f'{colors.RED}* git is not installed. Installing...{colors.RESET}\n')
        if iso == 'arch':
            install_cmd = 'sudo pacman -S git --noconfirm'
        elif iso == 'ubuntu':
            install_cmd = 'sudo apt install git -y'
        elif iso == 'wsl':
            install_cmd = 'sudo apt install git -y'

        os.system(install_cmd)
        print()

# run the playbook
def run_playbook(iso):
    if iso == 'arch':
        command = f'ansible-playbook --diff {DOTFILES_DIR}/playbooks/arch.yml'
        os.system(command)
    elif iso == 'ubuntu':
        command = f'ansible-playbook --diff {DOTFILES_DIR}/playbooks/ubuntu.yml'
        os.system(command)
    elif iso == 'wsl':
        command = f'ansible-playbook --diff {DOTFILES_DIR}/playbooks/wsl.yml'
        os.system(command)