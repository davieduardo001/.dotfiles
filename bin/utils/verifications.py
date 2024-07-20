import os
import subprocess
from utils.colors import colors

USER = os.getenv('USER')
HOSTNAME = os.getenv('HOSTNAME')
DOTFILES_DIR = '~/.dotfiles'
SSH_DIR = f'/home/{USER}/.ssh'

# check SDKMAN!
def is_sdkman_installed():
    sdkman_dir = os.path.expanduser('~/.sdkman')
    return os.path.exists(sdkman_dir) and os.path.isdir(sdkman_dir)

# install SDKMAN!
def install_sdkman():
    if is_sdkman_installed():
        print(f'{colors.GREEN}* SDKMAN! is already installed.{colors.RESET}\n')
    else:
        print(f'{colors.RED}* SDKMAN! is not installed. Installing...{colors.RESET}\n')
        install_cmd = 'curl -s "https://get.sdkman.io" | bash'
        os.system(install_cmd)
        print()

# check git
def is_git_installed():
    git_path = '/usr/bin/git'
    return os.path.exists(git_path) and os.path.isfile(git_path)

# install git
def install_git(iso):
    if is_git_installed():
        print(f'{colors.GREEN}* git is already installed.{colors.RESET}\n')
    else:
        print(f'{colors.RED}* git is not installed. Installing...{colors.RESET}\n')
        if iso == 'arch':
            os.system('sudo pacman -S git --noconfirm')
        elif iso == 'ubuntu' or iso == 'wsl':
            os.system('sudo apt install git -y')

        print(f'{colors.GREEN}* git is already installed.{colors.RESET}\n')

# check zip
def is_zip_installed():
    zip_dir = '/usr/bin/zip'
    return os.path.exists(zip_dir) and os.path.isfile(zip_dir)

# install zip
def intall_zip(iso):
    if is_zip_installed():
        print(f'{colors.GREEN}* zip installed{colors.RESET}\n')
    else:
        print(f'{colors.RED}* zip is not installed. Installing...{colors.RESET}\n')
        if iso == 'arch':
            os.system('sudo pacman -S zip --noconfirm')
        elif iso == 'ubuntu' or iso == 'wsl':
            os.system('sudo apt install zip -y')
        print(f'{colors.GREEN}* zip installed{colors.RESET}\n')

# check nvm
def is_nvm_installed():
    nvm_dir = os.path.expanduser('~/.nvm')
    return os.path.exists(nvm_dir) and os.path.isdir(nvm_dir)

# install nvm
def install_nvm():
    if is_nvm_installed():
        print(f'{colors.GREEN}* nvm installed{colors.RESET}\n')
    else:
        print(f'{colors.RED}* nvm is not installed. Installing...{colors.RESET}\n')
        os.system('curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash')
        print(f'{colors.GREEN}* nvm installed{colors.RESET}\n')

# check openssh:
def is_openssh_installed():
    openssh_dir = '/usr/bin/ssh'
    return os.path.exists(openssh_dir) and os.path.isfile(openssh_dir)

# check if ssh key where generated
def is_ssh_key_gen():
    id_rsa_dir = f'{SSH_DIR}/id_rsa'
    print(id_rsa_dir)
    return os.path.exists(id_rsa_dir) and os.path.isfile(id_rsa_dir)

# create ssh key
def create_ssh_key():
    if is_ssh_key_gen():
        print(f'{colors.GREEN}**** ssg key\'s where generated{colors.RESET}\n')
    else:
        print(f'{colors.RED}**** ssh key\'s where not generated{colors.RESET}\n')
        os.makedirs(SSH_DIR, exist_ok=True)
        os.chmod(SSH_DIR, 0o700)
        subprocess.run(['ssh-keygen', '-b', '4096', '-t', 'rsa', '-f', f"{SSH_DIR}/id_rsa", '-N', '', '-C', f"{USER}@{HOSTNAME}"], check=True)
        with open(f"{SSH_DIR}/id_rsa.pub", 'rb') as f_pub, open(f"{SSH_DIR}/authorized_keys", 'wb') as f_auth:
            f_auth.write(f_pub.read())
        os.chmod(f"{SSH_DIR}/authorized_keys", 0o600)
        print(f'{colors.GREEN}**** ssg key\'s where generated{colors.RESET}\n')

# create ssh key
def install_ssh():
    if is_openssh_installed():
        print(f'{colors.GREEN}* openssh installed{colors.RESET}\n')
        create_ssh_key()
    else:
        print(f'{colors.RED}* openssh is not installed. Installing...{colors.RESET}\n')
        create_ssh_key()
        print(f'{colors.GREEN}* openssh installed{colors.RESET}\n')

# check ansible
def is_ansible_installed():
    ansible_dir = '/usr/bin/ansible'
    return os.path.exists(ansible_dir) and os.path.exists(ansible_dir)

# install ansible
def install_ansible(iso):
    if is_ansible_installed():
        print(f'{colors.GREEN}* ansible installed{colors.RESET}\n')
    else:
        print(f'{colors.RED}* ansible is not installed. Installing...{colors.RESET}\n')
        if iso == 'arch':
            os.system('sudo pacman -S ansible --noconfirm')
        elif iso == 'ubuntu' or iso == 'wsl':
            os.system('sudo apt install ansible -y')
        print(f'{colors.GREEN}* ansible installed{colors.RESET}\n')

def update_system(iso):
    print(f'{colors.YELLOW}* upgrading system!{colors.RESET}\n')
    if iso == 'arch':
        os.system('sudo pacman -Syuu --noconfirm')
    elif iso == 'ubuntu' or iso == 'wsl':
        os.system('sudo apt update -y && sudo apt upgrade -y')
    print(f'{colors.GREEN}* system upgraded!\n{colors.RESET}')

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