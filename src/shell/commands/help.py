##
##  list_vms.py
##  src/shell/commands
##
##  Created by 0xGuigui on 25/03/2024.
##  Contributor(s): 0xGuigui
##

def run_help():
    help()

def help():
    """
    Display help message.
    """
    print("Available commands:\n")

    print("General:")
    print("  - help: Display this help message.")
    print("  - version: Display version information.")
    print("  - exit: Exit the program.")
    print("  - ls: List all files in the current directory with colors.")
    print("  - reload_commands: Reload the commands from the commands directory.\n")

    print("Datacenter Operations:")
    print("  - list_datacenters: List all datacenters in the vSphere environment.\n")

    print("VM Operations:")
    print("  - list_vms: List all VMs in the vSphere environment.")
    print("  - power_on_vm: Power on a specified VM.")
    print("  - power_off_vm: Power off a specified VM.")
    print("  - download_vm: Download a specified VM.\n")

    print("Snapshot Operations:")
    print("  - list_snapshot: List all snapshots for a specified VM.")
    print("  - create_snapshot: Create a snapshot for a specified VM.")
    print("  - revert_snapshot: Revert a specified VM to a specified snapshot.")
    print("  - delete_snapshot: Delete a specified snapshot from a specified VM.\n")

    print("Backup Operations:")
    print("  - list_backups: List all backups in the backup directory.\n")

    print("Server Information:")
    print("  - server_info: Display information about the vCenter Server.")