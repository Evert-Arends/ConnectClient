import requests
import constants as cfg


class Update:
    def __init__(self):
        if cfg.UPDATES is not True:
            pass
        else:
            print 'Checking for updates...'

    def check_for_update(self):
        r = requests.get()





