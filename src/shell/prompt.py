##
##  prompt.py
##  src/shell
##
##  Created by 0xGuigui on 13/03/2024.
##  Contributor(s): 0xGuigui
##

from include.lib import *
from include.funcs_library import *

def prompt(command):
    while True:
        cmd = input("SnakeShot > ")
        if cmd == "exit":
            print("Exiting SnakeShot")
            break
        elif cmd == "help":
            print("Available commands:")
            print("  - exit: Exit SnakeShot")
            print("  - help: Display this help message")
            print("  - list: List all VMs")
            print("  - snapshot: Create a snapshot")
            print("  - revert: Revert to a snapshot")
            print("  - delete: Delete a snapshot")
        elif cmd == "list":
            list_vms(si)
        elif cmd == "snapshot":
            create_snapshot(si)
        elif cmd == "revert":
            revert_snapshot(si)
        elif cmd == "delete":
            delete_snapshot(si)
        else:
            print("Unknown command. Type 'help' for available commands.")


            