##
##  prompt.py
##  src/shell
##
##  Created by 0xGuigui on 13/03/2024.
##  Contributor(s): 0xGuigui
##

import os
import importlib.util
import inspect
from glob import glob
from include.lib import vim
from include.funcs_library import *

def load_commands():
    """
    Load commands from the commands directory.
    """
    commands = {}
    command_files = glob("src/shell/commands/*.py")
    for file_path in command_files:
        file_name = os.path.basename(file_path)[:-3]  # Remove the .py extension
        spec = importlib.util.spec_from_file_location(file_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        commands[file_name] = module
    return commands

def prompt(si):
    """
    Prompt the user for commands.
    """
    content = si.RetrieveContent()
    about = content.about
    host_view = content.viewManager.CreateContainerView(content.rootFolder, [vim.HostSystem], True)
    hosts = host_view.view
    host_view.Destroy()

    commands = load_commands()
    while True:
        ip_address = hosts[0].summary.managementServerIp if hosts else "Unknown"  # Assuming there's at least one host
        user_input = input(f"SnakeShot - Server: {ip_address} > ").strip()
        if user_input == "exit":
            break
        else:
            user_input = user_input.split()
            command = user_input[0]
            args = user_input[1:]

            if command in commands:
                command_function = getattr(commands[command], f"run_{command}", None)
                if command_function:
                    # Get the parameters of the command function
                    params = inspect.signature(command_function).parameters

                    try:
                        # If 'si' is a parameter of the function, pass it
                        if 'si' in params:
                            command_function(si, *args)
                        else:
                            command_function(*args)
                    except Exception as e:
                        print(f"An error occurred while executing the command {command}: {e}")
                else:
                    print(f"Command {command} does not have a run_{command} function.")
            else:
                print("Command not found")