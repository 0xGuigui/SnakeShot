##
##  list_snapshot.py
##  src/shell/commands
##
##  Created by 0xGuigui on 25/03/2024.
##  Contributor(s): 0xGuigui
##

from include.lib import *

def run_list_snapshot(si):
    list_snapshot(si)

def list_snapshot(si):
    print("Do you want to list snapshots for all VMs or a specific VM?")
    print("1. All VMs")
    print("2. Specific VM")
    choice = input("Enter your choice: ")

    # If user wants to list snapshots for all VMs
    if choice == "1":
        content = si.RetrieveContent()
        container = content.viewManager.CreateContainerView(content.rootFolder, [vim.VirtualMachine], True)
        for vm in container.view:
            if vm.snapshot is not None:
                print(f"Snapshots for VM {vm.name}:")
                for snapshot in vm.snapshot.rootSnapshotList:
                    print(f"  - {snapshot.name}")
        container.Destroy()

    # If user wants to list snapshots for a specific VM
    elif choice == "2":
        vm_name = input("Enter the name of the VM: ")
        content = si.RetrieveContent()
        container = content.viewManager.CreateContainerView(content.rootFolder, [vim.VirtualMachine], True)
        for vm in container.view:
            if vm.name == vm_name:
                if vm.snapshot is not None:
                    print(f"Snapshots for VM {vm.name}:")
                    for snapshot in vm.snapshot.rootSnapshotList:
                        print(f"  - {snapshot.name}")
        container.Destroy()

    # If user enters an invalid choice
    else:
        print("Invalid choice")
        return