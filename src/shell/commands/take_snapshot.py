##
##  automate_tasks.py
##  src/shell/commands
##
##  Created by 0xGuigui on 15/04/2024.
##  Contributor(s): 0xGuigui
##

from include.lib import *
from lib.get_obj import *

def run_take_snapshot(si):
    take_snapshot(si)

def take_snapshot(si, vm_name=None):
    """
    Take a snapshot of a VM.
    """
    # Get the VMs
    content = si.RetrieveContent()

    # If no VM name is provided, ask the user
    if not vm_name:
        vm_name = input("Enter the name of the VM you want to take a snapshot of: ")

    # Get the VM
    vm = get_obj(content, [vim.VirtualMachine], vm_name)

    if not vm:
        print("Could not find a VM with the name ", vm_name)
        return

    # Check if the VM is powered on
    if vm.runtime.powerState == 'poweredOn':
        print("Warning: The VM is currently powered on. Taking a snapshot may take a long time and could potentially cause issues.")
        confirm = input("Do you want to continue? (yes/no): ")
        if confirm.lower() != 'yes':
            return

    # Ask the user for the snapshot name
    snapshot_name = input("Enter a name for the snapshot: ")

    # Take the snapshot
    task = vm.CreateSnapshot_Task(name=snapshot_name, memory=True, quiesce=True)
    while task.info.state == vim.TaskInfo.State.running:
        time.sleep(1)
    if task.info.state == vim.TaskInfo.State.success:
        print(f"Snapshot {snapshot_name} of VM {vm_name} created successfully.")
    else:
        print(f"Failed to create snapshot {snapshot_name} of VM {vm_name}.")