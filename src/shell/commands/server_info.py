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
    content = si.RetrieveContent()
    host = content.about.apiVersion
    print(f"Connected to the server with the API version {host}.")
    print(f"Server type: {content.about.apiType}")
    print(f"Server UUID: {content.about.instanceUuid}")
    print(f"Server name: {content.about.fullName}")
    print(f"Server version: {content.about.version}")
    print(f"Server build: {content.about.build}")
    print(f"Server ip: {content.about.ipAddress}")