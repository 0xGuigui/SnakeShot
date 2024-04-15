# SnakeShot

## 0.4.0
- Added version checking at program start
- Refactored check_update command to use the new version checking
- Refactored SnakeShot to be more pylint compliant
- Added basic webhook sender

## 0.3.1 (2024-04-15)
- Fixed useless dependencies

## 0.3.0 (2024-04-15)
- Added Changelog
- Added automated_task command to run automatically some tasks like backup, restore, etc scheduled
- Added check_update command to check for updates
- Added ls command to list files inside this directory
- Added take_snapshot command to take a snapshot of a VM
- Added vm_state command to get the state of a VM like powered on, powered off, ram, cpu, etc

## 0.2.0 (2024-04-02)
- Refacored vAuth for SSL certificate fix
- Disabled downloading of powered on VM for security reasons
- Refactored help command
- Refactored prompt to update server information printing and use hosts variable
- Added colored output for better readability

## 0.1.0 (2024-03-01)
- Initial release