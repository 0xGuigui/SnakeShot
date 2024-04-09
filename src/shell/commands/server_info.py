##
##  server_info.py
##  src/shell/commands
##
##  Created by 0xGuigui on 02/04/2024.
##  Contributor(s): 0xGuigui
##

from include.lib import *
from src.get_obj import *

def run_server_info(si):
    server_info(si)

def server_info(si):
    """
    Print information about the vSphere server.
    """
    content = si.RetrieveContent()
    about_info = content.about
    host_system = get_obj(content, [vim.HostSystem])

    print("Server information:")
    print(f"IP Address: {host_system.summary.managementServerIp}")
    print(f"Name: {about_info.name}")
    print(f"Full Name: {about_info.fullName}")
    print(f"Vendor: {about_info.vendor}")
    print(f"Version: {about_info.version}")
    print(f"Build: {about_info.build}")
    print(f"OS Type: {about_info.osType}")
    print(f"Product Line ID: {about_info.productLineId}")
    print(f"API Type: {about_info.apiType}")
    print(f"API Version: {about_info.apiVersion}")