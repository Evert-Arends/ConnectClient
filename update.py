import requests
import constants as cfg
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Disable insecure request message.
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class Update:
    def __init__(self):
        if cfg.UPDATES is not True:
            pass
        else:
            print 'Checking for updates...'
            self.check_for_update()

    @staticmethod
    def check_for_update():
        r = requests.get(url=cfg.VERSION_FILE, verify=False, timeout=5)
        if len(r.content) >= 5:
            print 'Repository seems down. Care to check?'
        else:
            version = float(r.content)
            if float(version) != cfg.VERSION:
                print 'Update available, check the repository to find out more.'
                print 'New version: {0}'.format(version)
                print 'Your version: {0}'.format(cfg.VERSION)
                return True
            else:
                return False
        return False


if __name__ == "__main__":
    update = Update.check_for_update()
    print update



