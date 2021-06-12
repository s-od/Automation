from re import A
import webbrowser, os, pathlib, time, sys, subprocess, pyautogui, urllib, requests, re, bs4, urllib
from os import system, name
from bs4 import BeautifulSoup
from pathlib import Path
from urllib import request
from urllib.request import urlopen
from setup import *

#paths
if os.name == 'nt':
    dp = str(Path.home() / "Downloads")
else:
    dp = str(os.path.join(Path.home(), "Downloads")) 
cf = dp + '/Core_automation_folder'  
imf = cf + '/Images'
ali = cf + '/Account_login_info'

#Path to verification text files
vocf = cf + '/var.txt'
voimf = imf + '/var.txt'
voali = ali + '/var.txt'

setup()


