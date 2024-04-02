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

    # Create a timestamp
    timestamp = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")

    # Create the directory if it doesn't exist
    directory = f"downloaded_vms/{vm_name}/{timestamp}"
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Get the OvfManager
    ovf_manager = si.content.ovfManager

    # Create an OvfCreateDescriptorParams object
    cdp = vim.OvfCreateDescriptorParams()

    # Export the VM to OVF
    ovf_descriptor = ovf_manager.CreateDescriptor(obj=vm, cdp=cdp)

    # Write the OVF descriptor to a file
    with open(f"{directory}/{vm_name}-{timestamp}.ovf", "w") as file:
        file.write(ovf_descriptor.ovfDescriptor)

    # Get a NFC lease for the VM
    lease = vm.ExportVm()

    # Wait for the lease to be ready
    while lease.state == vim.HttpNfcLease.State.initializing:
        time.sleep(1)

    if lease.state == vim.HttpNfcLease.State.ready:
        # Download each of the files in the lease
        for device_url in lease.info.deviceUrl:
            if device_url.disk:
                download_file(device_url.url, f"{directory}/{vm_name}-{timestamp}.vmdk")
            elif device_url.targetId.endswith('.nvram'):
                download_file(device_url.url, f"{directory}/{vm_name}-{timestamp}.nvram")

def download_file(url, filename):
    """
    Download a file from a URL.
    """
    response = requests.get(url, stream=True, verify=False)
    with open(filename, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)