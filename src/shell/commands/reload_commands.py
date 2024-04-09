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
    commands_dir = "src/shell/commands"
    sys.path.insert(0, commands_dir)

    for filename in os.listdir(commands_dir):
        if filename.endswith(".py"):
            module_name = filename[:-3]  # remove .py extension
            try:
                if module_name in sys.modules:
                    # If module is already imported, reload it
                    importlib.reload(sys.modules[module_name])
                else:
                    # Otherwise, import the module
                    importlib.import_module(module_name)
                print(f"Module {module_name} reloaded successfully.")
            except SyntaxError:
                print(f"Failed to reload module {module_name} due to syntax errors.")