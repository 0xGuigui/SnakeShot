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

import time

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
            tasks.append(run_download_vm)
        elif choice == '2':
            tasks.append(run_take_snapshot)
        elif choice == '3':
            tasks.append(run_power_off_vm)
        elif choice == '4':
            tasks.append(run_power_on_vm)
        elif choice == '5':
            print("Exiting automate tasks...")
            return
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

        print("Would you like add another task?")
        print("1. Yes")
        print("2. No")

        add_task = input("Enter your choice: ")

        if add_task != '1':
            break

    interval = input("Enter the interval in hours between task executions: ")
    interval = float(interval) * 60 * 60  # Convert hours to seconds

    print("Automating tasks...")
    try:
        while True:
            for task in tasks:
                task(si)
            print(f"Tasks completed. Waiting for {interval / 60 / 60} hours before next execution.")
            time.sleep(interval)
    except KeyboardInterrupt:
        confirm = input("Are you sure you want to stop the tasks? (yes/no): ")
        if confirm.lower() == 'yes':
            print("Stopping tasks...")
            return
        else:
            print("Resuming tasks...")