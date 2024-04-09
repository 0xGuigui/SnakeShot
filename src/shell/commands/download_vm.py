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
    load_from_file = input("Do you want to load VM names from a file? (Y/N): ")
    if load_from_file.lower() in ['y', 'yes']:
        file_path = input("Enter the path of the file containing VM names: ")
        if os.path.exists(file_path):
            if file_path.endswith('.csv'):
                with open(file_path, 'r') as file:
                    vm_names = [line.strip() for line in file]
            elif file_path.endswith('.txt'):
                with open(file_path, 'r') as file:
                    vm_names = [line.strip() for line in file]
            else:
                print("Unsupported file format. Only .csv and .txt files are supported.")
                return
        else:
            print("File not found.")
            return
    else:
        vm_names = input("Enter the name(s) of the VM(s) you want to download (comma-separated): ").split(',')

    download_vm(si, vm_names)

def download_vm(si, vm_names):
    """
    Download VMs.
    """
    for vm_name in vm_names:
        vm_name = vm_name.strip()
        content = si.RetrieveContent()
        vm = get_obj(content, [vim.VirtualMachine], vm_name)

        if not vm:
            print("Could not find a VM with the name ", vm_name)
            continue

        timestamp = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
        directory = f"downloaded_vms/{vm_name}/{timestamp}"
        if not os.path.exists(directory):
            os.makedirs(directory)

        ovf_manager = si.content.ovfManager
        cdp = vim.OvfCreateDescriptorParams()
        ovf_descriptor = ovf_manager.CreateDescriptor(obj=vm, cdp=cdp)

        with open(f"{directory}/{vm_name}-{timestamp}.ovf", "w") as file:
            file.write(ovf_descriptor.ovfDescriptor)

        lease = vm.ExportVm()
        while lease.state == vim.HttpNfcLease.State.initializing:
            time.sleep(1)

        if lease.state == vim.HttpNfcLease.State.ready:
            for device_url in lease.info.deviceUrl:
                if device_url.disk:
                    download_file(device_url.url, f"{directory}/{vm_name}-{timestamp}.vmdk")
                elif device_url.targetId.endswith('.nvram'):
                    download_file(device_url.url, f"{directory}/{vm_name}-{timestamp}.nvram")
                elif device_url.targetId.endswith('.mf'):
                    download_file(device_url.url, f"{directory}/{vm_name}-{timestamp}.mf")
                else:
                    print(f"Unknown file: {device_url.targetId}")

def download_file(url, filename, file_size=None):
    """
    Download a file from a URL.
    """
    response = requests.get(url, stream=True, verify=False)

    if file_size is None:
        content_length = response.headers.get('Content-Length')
        if content_length is not None:
            file_size = int(content_length)

    progress = tqdm(response.iter_content(8192), f"Downloading {filename}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024, bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}{postfix}]')

    with open(filename, 'wb') as file:
        for data in progress.iterable:
            file.write(data)
            progress.update(len(data))