from re import A
import webbrowser, os, pathlib, time, sys, subprocess, pyautogui, urllib, requests, re, bs4, urllib, random, string
from os import system, name
from bs4 import BeautifulSoup
from pathlib import Path
from urllib import request
from urllib.request import urlopen

if os.name == 'nt':
    dp = str(Path.home() / "Downloads")
else:
    dp = str(os.path.join(Path.home(), "Downloads")) 
cf = dp + '/Core_automation_folder'  
imf = cf + '/Images'
ali = cf + '/Account_login_info'

#def random_let(times=1):
#    for _ in range(times):
#        random.choice(string.ascii_letters)
#def random_num(times=1):
#    for _ in range(times):
#        a_raw = random.randint(0,9)
#        a = str(a_raw)


def mrin(times=8):
    f = open(ali + '/usernames.txt', 'w')
    for _ in range(times):
        isan = random.randint(1,2)
        if isan == 1:
            a_raw = random.randint(0,9)
            a = str(a_raw)
            f.write(a)
        elif isan == 2:
            a = random.choice(string.ascii_letters)

            

