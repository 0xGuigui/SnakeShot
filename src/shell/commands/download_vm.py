##
##  download_vm.py
##  src/shell/commands
##
##  Created by 0xGuigui on 02/04/2024.
##  Contributor(s): 0xGuigui
##

from include.lib import *
from src.get_obj import *

def run_download_vm(si):
    download_vm(si)

def download_vm(si):
    """
    Download a VM.
    """
    # Ask the user which vm (name) he wants to download
    vm_name = input("Enter the name of the VM you want to download: ")

    # Find the VM
    content = si.RetrieveContent()
    vm = get_obj(content, [vim.VirtualMachine], vm_name)

    if not vm:
        print("Could not find a VM with the name ", vm_name)
        return

    # Create the directory if it doesn't exist
    directory = "downloaded_vms/" + vm_name
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Get the OvfManager
    ovf_manager = si.content.ovfManager

    # Create an OvfCreateDescriptorParams object
    cdp = vim.OvfCreateDescriptorParams()

    # Export the VM to OVF
    ovf_descriptor = ovf_manager.CreateDescriptor(obj=vm, cdp=cdp)

    # Create a timestamp
    timestamp = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")

    # Write the OVF descriptor to a file
    with open(f"{directory}/{vm_name}-{timestamp}.ovf", "w") as file:
        file.write(ovf_descriptor.ovfDescriptor)