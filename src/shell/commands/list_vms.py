##
##  list_vms.py
##  src/shell/commands
##
##  Created by 0xGuigui on 25/03/2024.
##  Contributor(s): 0xGuigui
##

from include.lib import *

def run_list_vms(si):
    save_output = input("Would you like to save the output to a file? (Y/N) ")
    if save_output.lower() in ['o', 'oui', 'y', 'yes']:
        file_format = input("Choose the file format (1 for txt / 2 for csv): ")
        if file_format == '1':
            list_vms(si, 'txt')
        elif file_format == '2':
            list_vms(si, 'csv')
        else:
            print("Invalid choice. Please enter '1' for txt or '2' for csv.")
    else:
        list_vms(si)

def list_vms(si, file_format=None):
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

    # Print VM names or write to file
    if file_format:
        if file_format.lower() == 'txt':
            with open('vm_names.txt', 'w') as f:
                for vm_name in vm_names:
                    f.write(f"{vm_name}\n")
            print("VM names saved to vm_names.txt")
        elif file_format.lower() == 'csv':
            with open('vm_names.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                for vm_name in vm_names:
                    writer.writerow([vm_name])
            print("VM names saved to vm_names.csv")
    else:
        for vm_name in vm_names:
            print(vm_name)
    container.Destroy()