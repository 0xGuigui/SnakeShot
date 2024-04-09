##
##  list_datacenters.py
##  src/shell/commands
##
##  Created by 0xGuigui on 13/03/2024.
##  Contributor(s): 0xGuigui
##

from include.lib import *

def run_list_datacenters(si):
    list_datacenters(si)

def list_datacenters(si):
    """
    List all datacenters.
    """
    # Get content
    content = si.RetrieveContent()

    # Get datacenters
    datacenters = content.viewManager.CreateContainerView(content.rootFolder, [vim.Datacenter], True)

    # Print datacenters
    for dc in datacenters.view:
        print(dc.name)
    datacenters.Destroy()
