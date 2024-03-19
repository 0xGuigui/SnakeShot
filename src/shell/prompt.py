##
##  prompt.py
##  src/shell
##
##  Created by 0xGuigui on 13/03/2024.
##  Contributor(s): 0xGuigui
##

from include.lib import *
from include.funcs_library import *

def prompt():
    while True:
        command = input("SnakeShot $ ")
        if command == "exit":
            break
        elif command in os.listdir("src/shell/commands"):
            try:
                module = __import__(f"src.shell.commands.{command}", fromlist=[""])
                getattr(module, command)()
            except (ImportError, AttributeError):
                print(f"Error executing {command}")
        else:
            print("Command not found")