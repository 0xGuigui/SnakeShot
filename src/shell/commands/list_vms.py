##
##  list_vms.py
##  src/shell/commands
##
##  Created by 0xGuigui on 25/03/2024.
##  Contributor(s): 0xGuigui
##

from include.lib import *

def run_list_vms(si):
    """
    Run the VM listing and optionally save to a file.
    """
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
    content = si.RetrieveContent()

    container = content.viewManager.CreateContainerView(content.rootFolder, [vim.VirtualMachine], True)
    vm_names = [vm.name for vm in container.view]
    container.Destroy()

    vm_names.sort()

    if file_format:
        if file_format.lower() == 'txt':
            with open('vm_names.txt', 'w') as file:
                for vm_name in vm_names:
                    file.write(f"{vm_name}\n")
            print("VM names saved to vm_names.txt")
        elif file_format.lower() == 'csv':
            with open('vm_names.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                for vm_name in vm_names:
                    writer.writerow([vm_name])
            print("VM names saved to vm_names.csv")
    else:
        for vm_name in vm_names:
            print(vm_name)

# def list_vms(si, file_format=None):
#     """
#     List all VMs.
#     """
#     content = si.RetrieveContent()

#     container = content.viewManager.CreateContainerView(content.rootFolder, [vim.VirtualMachine], True)
#     vms = container.view
#     container.Destroy()

#     vms.sort(key=lambda vm: vm.name)

#     if file_format:
#         if file_format.lower() == 'txt':
#             with open('vms.txt', 'w') as file:
#                 for vm in vms:
#                     file.write(f"{vm.name}\n")
#             print("VM names saved to vms.txt")
#         elif file_format.lower() == 'csv':
#             with open('vms.csv', 'w', newline='') as file:
#                 writer = csv.writer(file)
#                 writer.writerow(["VM Name", "CPU", "RAM", "Storage", "Storage Used", "Storage Free", "RAM Usage", "CPU Usage"])
#                 for vm in vms:
#                     cpu = vm.config.hardware.numCPU
#                     ram = vm.config.hardware.memoryMB
#                     storage = sum([disk.capacityInKB for disk in vm.config.hardware.device if isinstance(disk, vim.vm.device.VirtualDisk)]) / 1024 / 1024
#                     storage_used = vm.summary.storage.committed / 1024 / 1024 / 1024
#                     storage_free = storage - storage_used
#                     ram_usage = vm.summary.quickStats.guestMemoryUsage
#                     ram_free = ram - ram_usage
#                     cpu_usage = vm.summary.quickStats.overallCpuUsage / 1000  # Convert MHz to GHz
#                     writer.writerow([vm.name, cpu, ram, storage, storage_used, storage_free, ram_usage, ram_free, cpu_usage])
#             print("VM details saved to vms.csv")
#     else:
#         for vm in vms:
#             print(vm.name)