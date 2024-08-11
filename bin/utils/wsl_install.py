import utils.verifications as verify
from utils.colors import colors

# install on wsl/ubuntu iso
def install_wsl():
    verify.update_system('wsl')
    verify.install_ansible('wsl')
    verify.install_sdkman()
    verify.install_git('wsl')
    verify.intall_zip('wsl')
    verify.install_nvm()
    verify.install_ssh()
    print(f'{colors.CYAN}* Play wsl playbook ***************{colors.RESET}\n')
    verify.run_playbook('wsl')

