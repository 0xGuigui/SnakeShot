##
##  reload_commands.py
##  src/shell/commands
##
##  Created by 0xGuigui on 08/04/2024.
##  Contributor(s): 0xGuigui
##

from include.lib import *

def run_reload_commands():
    reload_commands()

def reload_commands():
    commands_dir = "/src/shell/commands/"
    sys.path.insert(0, commands_dir)

    for file in os.listdir(commands_dir):
        if file.endswith('.py'):
            module_name = file[:-3]  # remove .py extension
            if module_name in sys.modules:
                # If the module was previously imported, reload it
                importlib.reload(sys.modules[module_name])
            else:
                # Otherwise, import the module
                globals()[module_name] = importlib.import_module(module_name)