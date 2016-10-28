import os

CONFIG_DIR = os.path.expanduser('~/.FireWallLogin')  # Path where data is stored
KEY_FILE = '{0}/user.txt'.format(CONFIG_DIR)  # File where data is stored
WRITE = False
USERNAME = None  # DO NOT PASTE YOUR USERNAME HERE!
PASSWORD = None  # DO NOT PASTE YOUR PASSWORD HERE!
MINUTES = 7
SSID = 'D105A'
RETRIEVE_SSID_COMMAND = 'iwgetid -r'
UPDATES = True
VERSION_FILE = 'https://raw.githubusercontent.com/Evert-Arends/ConnectClient/master/version.txt'
VERSION = 1.2
MESSAGE = 'Welcome to the connection bot. I\'m currently at version {0}, and still supported by the original' \
          ' developer!'.format(VERSION)

