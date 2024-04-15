##
##  power_on.py
##  src/shell/commands
##
##  Created by 0xGuigui on 02/04/2024.
##  Contributor(s): 0xGuigui
##

from include.lib import *
from lib.get_obj import *

def run_power_on_vm(si):
    vm_name = input("Enter the name of the VM you want to power on: ")
    power_on_vm(si, vm_name)

def power_on_vm(si, vm_name):
    content = si.RetrieveContent()
    vm = get_obj(content, [vim.VirtualMachine], vm_name)

    if vm:
        try:
            if vm.runtime.powerState == 'poweredOn':
                print(f"The virtual machine {vm_name} is already powered on.")
                return
            task = vm.PowerOnVM_Task()
            print(f"Powering on the virtual machine {vm_name}...")
        except Exception as e:
            print(f"An error occurred while powering on the virtual machine {vm_name}: {e}")
    else:
        print(f"Could not find a VM with the name {vm_name}.")