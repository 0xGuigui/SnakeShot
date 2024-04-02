##
##  list_vms.py
##  src/shell/commands
##
##  Created by 0xGuigui on 25/03/2024.
##  Contributor(s): 0xGuigui
##

from include.lib import *

def run_list_vms(si):
    list_vms(si)

def list_vms(si):
    """
    List all VMs.
    """

    # Get content
    content = si.RetrieveContent()

    # Get VMs
    container = content.viewManager.CreateContainerView(content.rootFolder, [vim.VirtualMachine], True)
    vm_names = [vm.name for vm in container.view]

    # Sort VM names
    vm_names.sort()

    # Print VM names
    for vm_name in vm_names:
        print(vm_name)
    container.Destroy()