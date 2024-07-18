import os
from utils.colors import colors

DOTFILES_DIR = '~/.dotfiles'

# check SDKMAN!
def is_sdkman_installed():
    # Check if the 'sdk' executable is in the PATH
    sdkman_dir = os.path.expanduser('~/.sdkman')
    if os.path.exists(sdkman_dir) and os.path.isdir(sdkman_dir):
        return 1
    return 0

# install SDKMAN!
def install_sdkman():
    # Install SDKMAN! using the provided installation command for Arch Linux
    if is_sdkman_installed() == 1:
        print(f'{colors.GREEN}SDKMAN! is already installed.{colors.RESET}\n')

    else:
        print(f'{colors.RED}SDKMAN! is not installed. Installing...{colors.RESET}\n')
        install_cmd = 'curl -s "https://get.sdkman.io" | bash'
        os.system(install_cmd)
        print()

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