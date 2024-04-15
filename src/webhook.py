##
##  webhook.py
##  src/auth
##
##  Created by 0xGuigui on 15/04/2024.
##  Contributor(s): 0xGuigui
##

from include.lib import *

def send_command_to_webhook(command):
    """
    Send a command to the Discord webhook.
    """
    webhook_url = None
    data = {
        "content": f"Command executed: {command}"
    }
    response = requests.post(webhook_url, data=json.dumps(data), headers={"Content-Type": "application/json"})
    if response.status_code != 204:
        raise ValueError(f"Request to webhook returned an error {response.status_code}, the response is:\n{response.text}")
