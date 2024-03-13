##
##  funcs_library.py
##  src
##
##  Created by 0xGuigui on 13/03/2024.
##  Contributor(s): 0xGuigui
##

from src.auth.vAuth import *

def auth_funcs():
    auth_funcs = [vAuth]
    for func in auth_funcs:
        func()

