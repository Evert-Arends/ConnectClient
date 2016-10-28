import requests
import constants as cfg


class Update:
    def __init__(self):
        if cfg.UPDATES is not True:
            pass
        else:
            print 'Checking for updates...'
            self.check_for_update()

    @staticmethod
    def check_for_update():
        r = requests.get(cfg.VERSION_FILE)
        return r.content


if __name__ == "__main__":
    update = Update.check_for_update()
    print update



