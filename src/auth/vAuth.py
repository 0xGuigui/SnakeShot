##
##  vAuth.py
##  src/auth
##
##  Created by 0xGuigui on 13/03/2024.
##  Contributor(s): 0xGuigui
##

from include.lib import *

def list_linked_vcenter_servers(si):
    """
    List all linked vCenter servers in the vSphere server.
    :param si: ServiceInstance, connection to the vSphere
    """
    content = si.RetrieveContent()
    linked_vcenters = content.setting.QueryOptions("VirtualCenter.LinkedView")
    if linked_vcenters:
        for vcenter in linked_vcenters:
            print("Linked vCenter Server:", vcenter.name)
    else:
        print("No linked vCenter servers found.")


def print_vcenter_info(si):
    """
    Print information about the vCenter Server.
    :param si: ServiceInstance, connection to the vCenter Server
    """
    about_info = si.content.about
    print("vCenter Server version:", about_info.version)
    print("vCenter Server build:", about_info.build)
    print("vCenter Server OS type:", about_info.osType)
    print("vCenter Server product name:", about_info.fullName)

def list_esxi_hosts(si):
    """
    List all ESXi hosts in the vSphere server.
    :param si: ServiceInstance, connection to the vSphere
    """
    content = si.RetrieveContent()
    container = content.viewManager.CreateContainerView(content.rootFolder, [vim.HostSystem], True)
    for esxi_host in container.view:
        print(esxi_host.name)

def vAuth():
    MAX_ATTEMPTS = 5
    attempts = 0

    ip_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")

    while attempts < MAX_ATTEMPTS:
        host = input("Enter the vSphere host: ")
        if not ip_pattern.match(host):
            print("Invalid IP address. Please enter a valid IP address in the format X.X.X.X")
            continue

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
            return si
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