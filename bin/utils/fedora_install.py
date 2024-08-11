import utils.verifications as verify
from utils.colors import colors

# install on fedora iso
def install_fedora():
    verify.update_system('fedora')
    verify.install_ansible('fedora')
    verify.install_sdkman()
    verify.install_git('fedora')
    verify.intall_zip('fedora')
    verify.install_nvm()
    verify.install_ssh()
    print(f'{colors.CYAN}* Play fedora playbook ***************{colors.RESET}\n')
    verify.run_playbook('fedora')
