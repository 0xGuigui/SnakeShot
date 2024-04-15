##
##  automate_tasks.py
##  src/shell/commands
##
##  Created by 0xGuigui on 15/04/2024.
##  Contributor(s): 0xGuigui
##


from include.lib import *
from src.shell.commands.download_vm import *
from src.shell.commands.take_snapshot import *
from src.shell.commands.power_off_vm import *
from src.shell.commands.power_on_vm import *
from lib.get_obj import *

def run_automate_tasks(si):
    automate_tasks(si)

def automate_tasks(si):
    """
    Automate tasks.
    """

    tasks = []

    while True:
        print("What tasks would you like to automate?")
        print("1. Download VMs")
        print("2. Take snapshots")
        print("3. Power off VMs")
        print("4. Power on VMs")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            tasks.append(run_download_vm(si))
        elif choice == '2':
            tasks.append(run_take_snapshot(si))
        elif choice == '3':
            tasks.append(run_power_off_vm(si))
        elif choice == '4':
            tasks.append(run_power_on_vm(si))
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

        print("Would you like add another task?")
        print("1. Yes")
        print("2. No")

        add_task = input("Enter your choice: ")

        if add_task != '1':
            break

    print("Automating tasks...")
    for task in tasks:
        task(si)