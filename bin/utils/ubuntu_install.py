import utils.verifications as verify
from utils.colors import colors

# install on ubuntu iso
def install_ubuntu():
    verify.update_system('ubuntu')
    verify.install_ansible('ubuntu')
    verify.install_oh_my_bash()
    verify.install_sdkman()
    verify.install_git('ubuntu')
    verify.intall_zip('ubuntu')
    verify.install_nvm()
    verify.install_ssh()
    print(f'{colors.CYAN}* Play ubuntu playbook ***************{colors.RESET}\n')
    verify.run_playbook('ubuntu')
