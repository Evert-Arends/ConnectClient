import os

CONFIG_DIR = os.path.expanduser('~/.FireWallLogin')  # Path where data is stored
KEY_FILE = '{0}/user.txt'.format(CONFIG_DIR)  # File where data is stored
WRITE = False
USERNAME = None
PASSWORD = None
MINUTES = 7
SSID = 'D105A'
RETRIEVE_SSID_COMMAND = 'iwgetid -r'
UPDATES = True