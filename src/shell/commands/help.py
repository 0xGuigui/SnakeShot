##
##  list_vms.py
##  src/shell/commands
##
##  Created by 0xGuigui on 25/03/2024.
##  Contributor(s): 0xGuigui
##

def run_help(si):
    help(si)

def help(si):
    """
    Display help message.
    """
    print("Available commands:")
    print("  - help: Display help message.")
    print("  - version: Display version information.")
    print("  - list_datacenters: List all datacenters.")
    print("  - list_vms: List all VMs.")
    print("  - list_snapshot: List all snapshots.")
    print("  - create_snapshot: Create a snapshot.")
    print("  - revert_snapshot: Revert a snapshot.")
    print("  - delete_snapshot: Delete a snapshot.")
    print("  - exit: Exit the program.")
    print("  - help: Display help message.")