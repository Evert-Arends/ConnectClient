#!/usr/bin/python
# Wide imports
import commands
import subprocess
import threading
from time import sleep

import requests
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from twisted.internet import task
from twisted.internet import reactor
from subprocess import check_output

import os
# Local imports
import constants as cfg

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
STATUS = ''
RETRIEVE_SSID_COMMAND = 'iwgetid -r'


def init():
    loginUrl = "https://10.0.101.1:8090/login.xml"
    print 'hey!'
    r = requests.get(loginUrl, verify=False)
    if not workingConnection():
        sys.exit("End of script, no use able network found.")

    if not check():
        cfg.USERNAME = raw_input("Please enter your username: ")
        cfg.PASSWORD = raw_input("Please enter your password: ")
        cfg.WRITE = True
    try:
        login(loginUrl, cfg.USERNAME, cfg.PASSWORD)
        STATUS = 'NOT NONE :D'
        return True
    except requests.ConnectionError:
        print 'well, that is wrong.. I guess,  whatever.'
        return False


def workingConnection(url='https://10.0.101.1:8090/httpclient.html', timeout=5, sslprotection=False):
    scanOutput = commands.getoutput(RETRIEVE_SSID_COMMAND)
    print scanOutput
    if 'D105A' not in scanOutput:
        print 'This seems to be the wrong SSID. Quitting now.'
        return False

    try:
        _ = requests.get(url=url, timeout=timeout, verify=sslprotection)
        return True
    except requests.ConnectionError:
        print 'The login resource is not available'
    return False


# Sending post request to the login API
def login(login_url, username, password):
    try:
        r = requests.post(login_url, data={'mode': 191, 'username': username, 'password': password}, verify=False)
    except requests.ConnectionError:
        print 'error'
        return False
    code = str(r.content)
    if not check_password(code):
        init()
    else:
        # print(r.status_code, r.reason, r.content)  # <--- Enable for logging
        if r.status_code == 200:
            print("Successfully logged in!")
            # Writes to file and sets writing to file to false
            if cfg.WRITE:
                write(cfg.USERNAME, cfg.PASSWORD)
                cfg.WRITE = False
            return True
        else:
            print ('There might be a problem, are you sure you are on the right network, with the right user details?')
            return False


# Checking if password file exists, and if it will set the global vars.
def check():
    if not os.path.exists(cfg.KEY_FILE):
        return
    else:
        key = open(cfg.KEY_FILE, 'r').read()
        userdetails = key.split(',')
        list(userdetails)
        # print "key:", userdetails <---- Enable for logging
        cfg.USERNAME = userdetails[0]
        cfg.PASSWORD = userdetails[1]

        # print "details", cfg.USERNAME, cfg.PASSWORD <--- Enable for logging
        return key


def check_password(code):
    if "password" not in code:
        return "ok"
    else:
        print("Wrong username or password, please try again.")
        return


def file_check():
    if not os.path.exists(cfg.CONFIG_DIR):
        os.mkdir(cfg.CONFIG_DIR)
        print('Created {0}'.format(cfg.CONFIG_DIR))


def write(username, password):
    file_check()
    write_string = (username + "," + password)
    open(cfg.KEY_FILE, 'w+').write(write_string)


if __name__ == "__main__":
    interval = (60 * cfg.MINUTES)
    # interval = (6)  # Testing purposes.
    try:
        l = task.LoopingCall(init)
        l.start(interval)
        # interval = 6  # Testing purposes.
        interval = (60 * cfg.MINUTES)
    except requests.ConnectionError:
        print 'Connection error, retrying in 3 seconds..'
        interval = 3
    reactor.run()

    # After the timer stops working.
    print ('Thanks for using me, and no, I won\'t report you :3')
