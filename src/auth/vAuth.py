##
##  vAuth.py
##  src/auth
##
##  Created by 0xGuigui on 13/03/2024.
##  Contributor(s): 0xGuigui
##

from include.lib import *

def vAuth():
    while True:
        host = input("Enter the vSphere host: ")
        user = input("Enter the vSphere username: ")
        pwd = getpass.getpass("Enter the vSphere password: ")

        # Création du contexte SSL sans vérification du certificat
        s = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        s.check_hostname = False
        s.verify_mode = ssl.CERT_NONE

        try:
            # Tentative de connexion avec le certificat SSL
            si = SmartConnect(host=host, user=user, pwd=pwd, sslContext=s)
            print("Connected to vSphere, with SSL certificate verification")
            break
        except ssl.SSLError as e:
            # En cas d'erreur SSL, demander à l'utilisateur s'il veut continuer
            print("SSL certificate verification failed:", e)
            choice = input("Continue connecting despite SSL certificate issue? (y/n): ").lower()
            if choice == 'y':
                # Demande de confirmation pour bypasser la vérification du certificat
                confirm = input("Are you sure you want to bypass SSL certificate verification? (y/n): ").lower()
                if confirm == 'y':
                    # Connexion sans vérification du certificat
                    si = SmartConnect(host=host, user=user, pwd=pwd)
                    print("Connected to vSphere (without SSL certificate verification)")
                    break
                else:
                    print("Returning to login.")
            else:
                print("Returning to login.")
        except Exception as e:
            print("Failed to connect:", e)
            return