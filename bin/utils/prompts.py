import os

# show menu for chose the instalation
def show_menu():
    print('1. Arch')
    print('2. Ubuntu')
    print('3. WSL')
    print('4. Fedora')
    print('5. Windows')

    return input('Select a option above: ')

# clear screen
def clear_screen():
    os_coiche = 'win' if os.name == 'nt' else 'linux'

    if os_coiche == 'win':
        _ = os.system('cls')
    elif os_coiche == 'linux':
        _ = os.system('clear')