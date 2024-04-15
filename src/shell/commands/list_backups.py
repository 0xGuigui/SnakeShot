##
##  list_backup.py
##  src/shell/commands
##
##  Created by 0xGuigui on 02/04/2024.
##  Contributor(s): 0xGuigui
##

from include.lib import *
from lib.get_obj import *

def run_list_backups(si):
    list_backups(si)

def list_backups(si):
    """
    List all the backups.
    """
    # Get the VMs
    content = si.RetrieveContent()
    vms = sorted(get_obj(content, [vim.VirtualMachine]), key=lambda vm: vm.name)

    # Loop through the VMs
    for vm in vms:
        # Get the VM name
        vm_name = vm.name

        # Get the directory
        directory = f"downloaded_vms/{vm_name}"

        # Check if the directory exists
        if os.path.exists(directory):
            # Get the backups
            backups = sorted(os.listdir(directory))

            # Loop through the backups
            for backup in backups:
                # Print the backup
                print(f"{vm_name}: {backup}")
        else:
            print(f"{vm_name}: No backups found")