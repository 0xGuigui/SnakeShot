##
##  power_off.py
##  src/shell/commands
##
##  Created by 0xGuigui on 02/04/2024.
##  Contributor(s): 0xGuigui
##

from include.lib import *
from src.get_obj import *

def run_power_off_vm(si):
    vm_name = input("Enter the name of the VM you want to power off: ")
    power_off_vm(si, vm_name)

def power_off_vm(si, vm_name, shutdown_type=None):
    content = si.RetrieveContent()
    vm = get_obj(content, [vim.VirtualMachine], vm_name)

    if vm:
        try:
            if vm.runtime.powerState == 'poweredOff':
                print(f"Virtual machine {vm_name} is already powered off.")
                return
            if shutdown_type is None:
                print("Choose the shutdown mode:")
                print("1. Guest OS shutdown")
                print("2. Power off")
                print("3. Immediate shutdown")
                shutdown_type = input("Enter your choice (1-3): ")
            if shutdown_type == '1':
                task = vm.ShutdownGuest()
                print(f"Guest OS of virtual machine {vm_name} is shutting down.")
            elif shutdown_type == '2':
                task = vm.PowerOffVM_Task()
                print(f"Virtual machine {vm_name} is powering off.")
            elif shutdown_type == '3':
                task = vm.TerminateVM()
                print(f"Virtual machine {vm_name} is shutting down immediately.")
            else:
                print("Invalid choice.")
        except Exception as e:
            print(f"An error occurred while shutting down the virtual machine {vm_name}: {str(e)}")
    else:
        print(f"Virtual machine {vm_name} was not found.")