##
##  vAuth.py
##  src/auth
##
##  Created by 0xGuigui on 13/03/2024.
##  Contributor(s): 0xGuigui
##

from include.lib import *

def vAuth():
    MAX_ATTEMPTS = 5
    attempts = 0

    ip_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")

    while attempts < MAX_ATTEMPTS:
        host = input("Enter the vSphere host: ")
        if not ip_pattern.match(host):
            print("Invalid IP address. Please enter a valid IP address in the format X.X.X.X")
            continue

        if os.path.isfile("config.json"):
            with open("config.json", "r") as f:
                config = json.load(f)
                if config.get("host") == host:
                    print("Using saved credentials")
                    user = config.get("user")
                    pwd = config.get("pwd")
                    si = connect_to_vsphere(host, user, pwd)
                    if si:
                        return si

        user = input("Enter the vSphere username: ")
        pwd = getpass.getpass("Enter the vSphere password: ")

        si = connect_to_vsphere(host, user, pwd)
        if si:
            save = input("Do you want to save these credentials? (y/n): ").lower()
            if save == 'y':
                with open("config.json", "w") as f:
                    json.dump({"host": host, "user": user, "pwd": pwd}, f)
                print("Credentials saved to config.json")
            return si

        attempts += 1

    print("Maximum login attempts exceeded.")
    return None

def connect_to_vsphere(host, user, pwd):
    s = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    s.check_hostname = False
    s.verify_mode = ssl.CERT_NONE

    try:
        si = vim.SmartConnect(host=host, user=user, pwd=pwd, sslContext=s)
        print("Connected to vSphere")
        return si
    except ssl.SSLError as e:
        print("SSL certificate verification failed:", e)
        choice = input("Continue connecting despite SSL certificate issue? (y/n): ").lower()
        if choice != 'y':
            print("Returning to login.")
            return None
        confirm = input("Are you sure you want to bypass SSL certificate verification? (y/n): ").lower()
        if confirm != 'y':
            print("Returning to login.")
            return None
    except Exception as e:
        print("Failed to connect:", e)
        return None

    print("Connected to vSphere (without SSL certificate verification)")
    return si
