##
##  vAuth.py
##  src/auth
##
##  Created by 0xGuigui on 13/03/2024.
##  Contributor(s): 0xGuigui
##

from include.lib import *

def vAuth():
    MAX_ATTEMPTS = 3
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
                    try:
                        si = SmartConnect(host=host, user=user, pwd=pwd)
                        print("Connected to vSphere")
                        return si
                    except VimException as ve:
                        print("Failed to connect:", ve)
                    attempts += 1
                    continue

        user = input("Enter the vSphere username: ")
        pwd = getpass.getpass("Enter the vSphere password: ")

        s = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        s.verify_mode = ssl.CERT_NONE  # Ne pas vérifier le certificat

        try:
            si = SmartConnect(host=host, user=user, pwd=pwd, sslContext=s)
            print("Connected to vSphere")
            save = input("Do you want to save these credentials? (y/n): ").lower()
            if save == 'y':
                with open("config.json", "w") as f:
                    json.dump({"host": host, "user": user, "pwd": pwd}, f)
                print("Credentials saved to config.json")
            return si
        except ssl.SSLError as e:
            print("SSL certificate verification failed:", e)
            choice = input("Continue connecting despite SSL certificate issue? (y/n): ").lower()
            if choice != 'y':
                print("Returning to login.")
        except VimException as ve:
            print("Failed to connect:", ve)

        attempts += 1

    print("Maximum login attempts exceeded.")
    return None
