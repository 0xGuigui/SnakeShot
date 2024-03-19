##
##  prompt.py
##  src/shell
##
##  Created by 0xGuigui on 13/03/2024.
##  Contributor(s): 0xGuigui
##

from include.lib import *
from include.funcs_library import *
import os
import importlib.util
from glob import glob

def load_commands():
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
    commands = load_commands()
    while True:
        user_input = input("SnakeShot $ ")
        if user_input == "exit":
            break
        elif user_input in commands:
            command_function = getattr(commands[user_input], f"run_{user_input}", None)
            if command_function:
                command_function(si)
            else:
                print(f"Command {user_input} does not have a run_{user_input} function.")
        else:
            print("Command not found")
