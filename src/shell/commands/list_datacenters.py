##
##  list_datacenters.py
##  src/shell/commands
##
##  Created by 0xGuigui on 13/03/2024.
##  Contributor(s): 0xGuigui
##

from include.lib import *


def list_datacenters(si):
    """
    List all datacenters.
    """
    content = si.RetrieveContent()
    datacenters = content.viewManager.CreateContainerView(content.rootFolder, [vim.Datacenter], True)
    for dc in datacenters.view:
        print(dc.name)
    datacenters.Destroy()
