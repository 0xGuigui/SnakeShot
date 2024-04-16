##
##  backup_vm.py
##  src/shell/commands
##
##  Created by 0xGuigui on 16/04/2024.
##  Contributor(s): 0xGuigui
##

from include.lib import *
from lib.get_obj import *

def run_backup_vm(si):
    """
    Run the backup VM process.
    """
    load_from_file = input("Do you want to load VM names from a file? (Y/N): ")
    if load_from_file.lower() in ['y', 'yes']:
        file_path = input("Enter the path of the file containing VM names: ")
        if os.path.exists(file_path):
            if file_path.endswith('.csv') or file_path.endswith('.txt'):
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

    for vm_name in vm_names:
        backup_vm(si, vm_name.strip())

def backup_vm(si, vm_name):
    """
    Download a VM.
    """
    content = si.RetrieveContent()
    vm = get_obj(content, [vim.VirtualMachine], vm_name)

    if not vm:
        print(f"Could not find a VM with the name {vm_name}")
        return

    vmdk_size = sum([disk.capacityInKB for disk in vm.config.hardware.device if isinstance(disk, vim.vm.device.VirtualDisk)]) / 1024 / 1024

    if vm.runtime.powerState == 'poweredOn':
        print(f"Downloading of VM {vm_name} has been disabled by SnakeShot for security reasons, please power off the VM before downloading it.")
        print(f"Refer to the VMWare documentation for more information on how to download a powered on VM: https://kb.vmware.com/s/article/1006333")
        return

    timestamp = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
    directory = f"downloaded_vms/{vm_name}/{timestamp}"
    os.makedirs(directory, exist_ok=True)

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
                download_file(device_url.url, f"{directory}/{vm_name}-{timestamp}.vmdk", vmdk_size)
            # elif device_url.targetId.endswith('.nvram'):
            #     download_file(device_url.url, f"{directory}/{vm_name}-{timestamp}.nvram")
            # elif device_url.targetId.endswith('.mf'):
            #     download_file(device_url.url, f"{directory}/{vm_name}-{timestamp}.mf")
            else:
                print(f"Unknown file: {device_url.targetId}")

    # Compress the directory
    subprocess.run(["zstd", "-r", directory], check=True)

def download_file(url, filename, file_size=None):
    """
    Download a file from a URL.
    """
    try:
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
    except Exception as e:
        print(f"An error occurred while downloading the VM: {e}")