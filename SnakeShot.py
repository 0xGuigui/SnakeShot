##
##  SnakeShot.py
##  SnakeShot
##
##  Created by 0xGuigui on 13/03/2024.
##  Contributor(s): 0xGuigui
##

from include.lib import *
from include.funcs_library import *

def main():
    print ("Welcome to SnakeShot, the vSphere inventory tool")
    print ("This tool will list all ESXi hosts in the vSphere server and print information about the vCenter Server.")
    print ("Developed by 0xGuigui")
    print ("https://github.com/0xGuigui/SnakeShot")
    print ("Version: ", version_number())

    try:
        si = vAuth()
        if si is not None:
            prompt(si)
        else:
            print("Failed to connect to vSphere")
    except KeyboardInterrupt:
        print("\nUser interrupted the program, exiting...")

if __name__ == "__main__":
    main()