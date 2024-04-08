##
##  ls.py
##  src/shell/commands
##
##  Created by 0xGuigui on 08/04/2024.
##  Contributor(s): 0xGuigui
##

from include.lib import *

def run_ls():
    ls()

def ls():
    """
    List all files in the current directory.
    """
    init(autoreset=True)
    files = os.listdir('.')
    for file in files:
        if os.path.isdir(file):
            print(Fore.BLUE + file)
        elif os.path.isfile(file) and os.access(file, os.X_OK):
            print(Fore.GREEN + file)
        elif file.startswith('.'):
            print(Fore.LIGHTBLACK_EX + file)
        else:
            print(Style.RESET_ALL + file)