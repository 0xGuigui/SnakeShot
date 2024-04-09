##
##  get_obj.py
##  src
##
##  Created by 0xGuigui on 02/04/2024.
##  Contributor(s): 0xGuigui
##

from include.lib import *

def get_obj(content, vimtype, name=None):
    """
    Get the vsphere object associated with a given text name.
    """
    obj = None
    container = content.viewManager.CreateContainerView(content.rootFolder, vimtype, True)
    if name:
        for c in container.view:
            if c.name == name:
                obj = c
                break
    else:
        obj = container.view
    return obj