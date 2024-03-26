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
        else:
            user_input = user_input.split()
            command = user_input[0]
            args = user_input[1:]

            if command in commands:
                command_function = getattr(commands[command], f"run_{command}", None)
                if command_function:
                    try:
                        # Essayer d'exécuter la fonction avec le paramètre 'si' et les arguments supplémentaires
                        command_function(si, *args)
                    except TypeError:
                        try:
                            # Si cela échoue, essayer d'exécuter la fonction avec seulement le paramètre 'si'
                            command_function(si)
                        except TypeError:
                            try:
                                # Si cela échoue aussi, essayer d'exécuter la fonction sans aucun paramètre
                                command_function()
                            except Exception as e:
                                print(f"An error occurred while executing the command {command}: {e}")
                else:
                    print(f"Command {command} does not have a run_{command} function.")
            else:
                print("Command not found")