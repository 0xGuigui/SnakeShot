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
                        # Connexion avec les informations de connexion sauvegardées
                        s = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
                        s.check_hostname = False
                        s.verify_mode = ssl.CERT_NONE
                        si = SmartConnect(host=host, user=user, pwd=pwd)
                        print("Connected to vSphere")
                        return si
                    except Exception as e:
                        print("Failed to connect:", e)
                    attempts += 1
                    continue

        user = input("Enter the vSphere username: ")
        pwd = getpass.getpass("Enter the vSphere password: ")

        # Création du contexte SSL sans vérification du certificat
        s = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        s.check_hostname = True
        s.verify_mode = ssl.CERT_REQUIRED

        try:
            # Tentative de connexion avec le certificat SSL
            si = SmartConnect(host=host, user=user, pwd=pwd, sslContext=s)
            print("Connected to vSphere, with SSL certificate verification")
            # save = input("Do you want to save these credentials? (y/n): ").lower()
            # if save == 'y':
            #     # Sauvegarde des informations de connexion
            #     with open("config.json", "w") as f:
            #         json.dump({"host": host, "user": user, "pwd": pwd}, f)
            #     print("Credentials saved to config.json")
            # return si
        except ssl.SSLError as e:
            # En cas d'erreur SSL, demander à l'utilisateur s'il veut continuer
            print("SSL certificate verification failed:", e)
            choice = input("Continue connecting despite SSL certificate issue? (y/n): ").lower()
            if choice == 'y':
                # Demande de confirmation pour bypasser la vérification du certificat
                print("By bypassing, your connection will be less secure, and may be vulnerable to MITM attacks, or other security threats. SnakeShot is not responsible for any security breaches that may occur as a result of bypassing SSL certificate verification.")
                confirm = input("Are you sure you want to bypass SSL certificate verification? (y/n): ").lower()
                if confirm == 'y':
                    # Connexion sans vérification du certificat
                    s = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
                    s.check_hostname = False
                    s.verify_mode = ssl.CERT_NONE
                    si = SmartConnect(host=host, user=user, pwd=pwd, sslContext=s)
                    print("Connected to vSphere (without SSL certificate verification)")
                    return si
                else:
                    print("Returning to login.")
            else:
                print("Returning to login.")
        except Exception as e:
            print("Failed to connect:", e)

        attempts += 1

    print("Maximum login attempts exceeded.")
    return None
