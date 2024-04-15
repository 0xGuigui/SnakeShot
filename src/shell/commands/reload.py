##
##  reload.py
##  src/shell/commands
##
##  Created by 0xGuigui on 15/04/2024.
##  Contributor(s): 0xGuigui
##

from include.lib import *
from lib.get_obj import *

def run_reload(si):
    reload(si)

def reload(si):
    with open(__file__, 'r') as file:
        script = file.read()
    exec(script)