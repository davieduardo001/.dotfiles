import utils.verifications as verify
from utils.colors import colors

# install on arch
def install_sdkman():
    verify.install_sdkman()
    print(f'{colors.CYAN}* Play arch playbook ***************{colors.RESET}\n')
    verify.run_playbook('arch')


