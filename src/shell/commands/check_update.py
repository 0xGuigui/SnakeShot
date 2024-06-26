##
##  check_update.py
##  src/shell/commands
##
##  Created by 0xGuigui on 15/04/2024.
##  Contributor(s): 0xGuigui
##

from include.lib import *
from include.funcs_library import *

def run_check_update():
    check_update()

def check_update():
    """
    Check for updates.
    """
    # Download the file from GitHub
    response = requests.get("https://raw.githubusercontent.com/0xGuigui/SnakeShot/main/src/shell/commands/version.py")
    github_file = response.text

    # Read the local file
    with open("src/shell/commands/version.py", "r") as file:
        local_file = file.read()

    # Parse the files
    github_ast = ast.parse(github_file)
    local_ast = ast.parse(local_file)

    # Extract the version number
    github_version = [node.value.s for node in ast.walk(github_ast) if isinstance(node, ast.Assign) and node.targets[0].id == "version_number"][0]
    local_version = [node.value.s for node in ast.walk(local_ast) if isinstance(node, ast.Assign) and node.targets[0].id == "version_number"][0]

    # Compare the version numbers
    if github_version == local_version:
        print(f"{Fore.GREEN}The program is up to date.{Style.RESET_ALL}")
    elif github_version > local_version:
        print("An update is available.")
        # Download the changelog
        response = requests.get("https://raw.githubusercontent.com/0xGuigui/SnakeShot/main/CHANGELOG.md")
        changelog = response.text
        # Extract the update information for the latest version
        match = re.search(rf"## {re.escape(github_version)} \(.*?\)(.*?)##", changelog, re.DOTALL)
        if match:
            update_info = match.group(1).strip()
            print("Update information:")
            print(update_info)
        else:
            print("Could not find update information for the latest version.")

        # Ask the user if they want to update
        confirm = input("Do you want to update the program? (yes/no): ")
        if confirm.lower() == 'yes':
            # Update the program
            os.system("git clone https://github.com/0xGuigui/SnakeShot.git")
            print("The program has been updated. Please restart the program.")
    else:
        print("Version mismatch, probably due to a local development version.")