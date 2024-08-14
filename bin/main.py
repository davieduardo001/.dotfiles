from utils.colors import colors
import utils.prompts as p
import utils.arch_install as arch
import utils.wsl_install as wsl
import utils.ubuntu_install as ubuntu
import utils.fedora_install as fedora

def main():
    p.clear_screen()

    print(f'\n{colors.YELLOW}STARTING THE CONFIG FILE{colors.RESET}\n')

    installation_option = p.show_menu()

    if installation_option == '1':
        p.clear_screen()
        print(f'{colors.CYAN}* Arch instalation ***************{colors.RESET}\n')
        arch.install_arch()

    elif installation_option == '2':
        p.clear_screen()
        print(f'{colors.CYAN}Ubuntu installation{colors.RESET}\n')
        ubuntu.install_ubuntu()

    elif installation_option == '3':
        p.clear_screen()
        print(f'{colors.CYAN}WSL installation ***************{colors.RESET}\n')
        wsl.install_wsl()

    elif installation_option == '4':
        p.clear_screen()
        print(f'{colors.CYAN}RedHat installation ***************{colors.RESET}\n')
        fedora.install_fedora()

    elif installation_option == '5':
        p.clear_screen()
        print(f'{colors.RED}U\'ll need to run the win instalation with the powershell exec{colors.RESET}\n\n{colors.CYAN}More instructions on the README win installation session\n')

    else:
        p.clear_screen()
        print(f'{colors.RED}Option did\'t found!{colors.RESET}\n')

main()