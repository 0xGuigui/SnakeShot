##
##  vm_infos.py
##  src/shell/commands
##
##  Created by 0xGuigui on 15/04/2024.
##  Contributor(s): 0xGuigui
##

from include.lib import *
from lib.get_obj import *

def run_vm_infos(si):
    """
    Run VM state.
    """
    vm_infos(si)

def vm_infos(si, vm_name=None):
    """
    Get the state of a VM.
    """
    # Get the VMs
    content = si.RetrieveContent()

    # If no VM name is provided, ask the user
    if not vm_name:
        vm_name = input("Enter the name of the VM you want to check the state of: ")

    # Get the VM
    vm = get_obj(content, [vim.VirtualMachine], vm_name)

    if not vm:
        print("Could not find a VM with the name ", vm_name)
        return

    # Get the VM state
    state = vm.runtime.powerState

    # Print the VM state
    if state == 'poweredOn':
        print(f"{Fore.GREEN}VM {vm_name} is powered on.{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}VM {vm_name} is powered off.{Style.RESET_ALL}")

    # Get the VM resources
    cpu = vm.config.hardware.numCPU
    memory = vm.config.hardware.memoryMB
    storage = sum([disk.capacityInKB for disk in vm.config.hardware.device if isinstance(disk, vim.vm.device.VirtualDisk)])

    # Print the VM resources
    print(f"CPU: {cpu} cores")
    print(f"Memory: {memory} MB")
    print(f"Storage: {storage / 1024 / 1024} GB")

    # Get the VM resource usage
    cpu_usage = vm.summary.quickStats.overallCpuUsage
    memory_usage = vm.summary.quickStats.guestMemoryUsage
    storage_usage = vm.summary.storage.committed / 1024 / 1024 / 1024

    # Print the VM resource usage
    print(f"CPU Usage: {cpu_usage} MHz")
    print(f"Memory Usage: {memory_usage} MB")
    # Arrondi à 2 chiffres après la virgule
    print(f"Storage Usage: {storage_usage:.2f} GB")