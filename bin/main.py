from utils.colors import colors
import utils.prompts as p
import utils.arch_install as arch

def main():
    print(f'\n{colors.YELLOW}STARTING THE CONFIG FILE{colors.RESET}\n')
    
    installation_option = p.show_menu()

    if installation_option == '1':
        p.clear_screen()
        print(f'{colors.CYAN}Arch instalation{colors.RESET}\n')
        arch.install_sdkman()

    elif installation_option == '2':
        p.clear_screen()
        print(f'{colors.CYAN}Ubuntu installation{colors.RESET}\n')

    else:
        p.clear_screen()
        print(f'{colors.RED}Option did\'t found!{colors.RESET}\n')

main()