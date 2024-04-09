##
##  lib.py
##  include
##
##  Created by 0xGuigui on 13/03/2024.
##  Contributor(s): 0xGuigui
##

# Imports all the necessary libraries
import sys
import ssl
import getpass
import re
import requests
import json
import os
import subprocess
import importlib
import csv
import time
import inspect

from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim, vmodl
from datetime import datetime
from tqdm import tqdm
from termcolor import colored