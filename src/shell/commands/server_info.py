##
##  server_info.py
##  src/shell/commands
##
##  Created by 0xGuigui on 02/04/2024.
##  Contributor(s): 0xGuigui
##

from include.lib import *
from src.get_obj import *

def run_server_info(si):
    server_info(si)

def server_info(si):
    content = si.RetrieveContent()
    host = content.about.apiVersion
    print(f"Connected to the server with the API version {host}.")
    print(f"Server type: {content.about.apiType}")
    print(f"Server UUID: {content.about.instanceUuid}")
    print(f"Server name: {content.about.fullName}")
    print(f"Server version: {content.about.version}")
    print(f"Server build: {content.about.build}")
    print(f"Server locale: {content.locale}")
    print(f"Server time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Server current time: {content.currentTime.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Server uptime: {content.currentTime - content.about.currentTime}")
    print(f"Server IP: {content.about.client.ipAddress}")
    print(f"Server session ID: {content.sessionManager.currentSession.key}")
    print(f"Server user: {content.sessionManager.currentSession.userName}")
    print(f"Server user type: {content.sessionManager.currentSession.loginTime}")
    print(f"Server session timeout: {content.sessionManager.currentSession.sessionTimeout}")
    print(f"Server session locale: {content.sessionManager.currentSession.locale}")
    print(f"Server session message locale: {content.sessionManager.currentSession.messageLocale}")