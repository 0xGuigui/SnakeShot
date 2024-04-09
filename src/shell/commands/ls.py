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
    files = os.listdir('.')
    for file in files:
        if os.path.isdir(file):
            print(Fore.BLUE + file + Style.RESET_ALL)  # Blue for directories
        elif os.path.isfile(file) and os.access(file, os.X_OK):
            print(Fore.LIGHTGREEN_EX + file + Style.RESET_ALL)  # Light green for executable files
        elif file.startswith('.'):
            print(Fore.LIGHTBLACK_EX + file + Style.RESET_ALL)  # Dark grey for hidden files
        else:
            print(file)  # White for other files