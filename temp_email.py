from re import A
import webbrowser, os, pathlib, time, sys, subprocess, pyautogui, urllib, requests, re, bs4, urllib
from os import system, name
from bs4 import BeautifulSoup
from pathlib import Path
from urllib import request
from urllib.request import urlopen

#paths
if os.name == 'nt':
    dp = str(Path.home() / "Downloads")
else:
    dp = str(os.path.join(Path.home(), "Downloads")) 
cf = dp + '/Core_automation_folder'  
imf = cf + '/Images'
ali = cf + '/Account_login_info'



def temp_email():
    webbrowser.open_new_tab(url='https://temp-mail.org/en/change')
    time.sleep(5)
    for _ in range(7):
        pyautogui.press('Tab')
    pyautogui.press('Enter')
    

temp_email()