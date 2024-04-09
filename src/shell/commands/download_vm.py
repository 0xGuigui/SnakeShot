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
    save_to_file = input("Would you like to save the list of VMs to a file? (Y/N) ")
    if save_to_file.lower() in ['o', 'oui', 'y', 'yes']:
        file_format = input("Choose the file format (txt/csv): ")
        file_path = input("Enter the path to save the file: ")
        if file_format.lower() in ['txt', 'csv']:
            download_vm(si, save_to_file=True, file_format=file_format.lower(), file_path=file_path)
        else:
            print("Unsupported file format. Supported formats are txt and csv.")
    else:
        download_vm(si)

def download_vm(si, save_to_file=False, file_format=None, file_path=None):
    """
    Download a VM and its associated files.
    """
    # Ask the user which VM (name) they want to download
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
            elif device_url.targetId.endswith('.mf'):
                download_file(device_url.url, f"{directory}/{vm_name}-{timestamp}.mf")
            else:
                print(f"Unknown file: {device_url.targetId}")

    # Save VM list to file if requested
    if save_to_file and file_format and file_path:
        save_vm_list(vm_name, timestamp, file_format, file_path)

def save_vm_list(vm_name, timestamp, file_format, file_path):
    """
    Save VM list to a file (txt or csv).
    """
    vm_data = [vm_name, timestamp]
    if file_format == 'txt':
        with open(file_path, 'a') as file:
            file.write(f"VM Name: {vm_name}, Timestamp: {timestamp}\n")
    elif file_format == 'csv':
        with open(file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(vm_data)

def download_file(url, filename, file_size=None):
    """
    Download a file from a URL.
    """
    response = requests.get(url, stream=True, verify=False)

    # If file size is not provided, try to get it from the response headers
    if file_size is None:
        content_length = response.headers.get('Content-Length')
        if content_length is not None:
            file_size = int(content_length)

    # Create a progress bar
    progress = tqdm(response.iter_content(8192), f"Downloading {filename}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024, bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}{postfix}]')

    with open(filename, 'wb') as file:
        for data in progress.iterable:
            # Write data read to the file
            file.write(data)

            # Update the progress bar
            progress.update(len(data))