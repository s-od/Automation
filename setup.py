########################################################################################
# This File is testing the program before adding it to the main.py just incase of bugs #
########################################################################################

from re import A
import webbrowser, os, pathlib, time, sys, subprocess, pyautogui, urllib, requests, re, bs4, urllib
from os import system, name
from bs4 import BeautifulSoup
from pathlib import Path
from urllib import request
from urllib.request import urlopen


##############################################
# F is Saved for opening of files like .txts #
##############################################

#############################################
# Need to add GUI to the program Later!     #
#############################################

#Path to folders
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
#True statement
Tstate = True

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def cas(file):
    f = open(file,'x')
    f.write('########################          #\n')
    f.write('########################         # \n')
    f.write('## CHECKED AND STABLE ##    #   #  \n')
    f.write('########################     # #   \n')
    f.write('########################      #    \n')
    f.close()

def setup():
    #file storage
    try:
        f = open(vocf, 'r')
        f.close()
    except FileNotFoundError:
        os.mkdir(cf)
        cas(vocf)
    try:
        f = open(voimf, 'r')
        f.close()
    except FileNotFoundError:
        os.mkdir(imf)
        cas(voimf)
    try:
        f = open(voali, 'r')
        f.close()
    except FileNotFoundError:
        os.mkdir(ali)
        cas(voali)
    #Check if modules are installed
    print('Requirements:\n- Pyautogui\n- Requests\n- BeautifulSoup4')
    time.sleep(.5)
    try:
        import pyautogui
    except ImportError:
        print('Pyautogui Not found. Downloading')
        subprocess.check_call([sys.executable, "-m", "pip", "install", 'pyautogui'])
    finally:
        print('Importing...')
        time.sleep(.5)
        print('If there is an error importing, restart the program if not install it manually!')
        time.sleep(.5)
        import pyautogui
    try:
        import requests
    except ImportError:
        print('Pyautogui Not found. Downloading')
        subprocess.check_call([sys.executable, "-m", "pip", "install", 'requests'])
    finally:
        print('Importing...')
        time.sleep(.5)
        print('If there is an error importing, restart the program if not install it manually!')
        time.sleep(.5)
        import requests
    try:
        import bs4
    except ImportError:
        print('Pyautogui Not found. Downloading')
        subprocess.check_call([sys.executable, "-m", "pip", "install", 'bs4'])
    finally:
        print('Importing...')
        time.sleep(.5)
        print('If there is an error importing, restart the program if not install it manually!')
        time.sleep(.5)
        import bs4
    
    #Image file location
    try:
        f = open(imf + '/image_config.txt','r')
        f.close()
    except FileNotFoundError:
        f = open(imf + '/image_config.txt', 'x')
        imgloc = input('Image Location ')
        f.writelines(imgloc +'\n')
        f.close()
        print(f'The profile picture location is {imgloc}')
        time.sleep(.1)
        print(f'To change the location of this file go to {imf}/image_config.txt')

    #Password details
    try:
        f = open(ali + '/password_for_accounts.txt','r')
        f.close()
    except FileNotFoundError:
        f = open(ali + '/password_for_accounts.txt', 'x')
        while True:
            psswordfac = input('Password for all of the Accounts: ')
            if psswordfac == ('1234' or '1234567890' or '12345' or '123456' or '1234567' or '12345678' or '123456789'):
                clear()
                print('Password too weak!')
            elif len(psswordfac) < 8:
                clear()
                print('Password Not long enough, Needs to be 8 characters long!')
            else:
                clear()
                psswordfacvar = input('Retype your password: ')
                if psswordfac == psswordfacvar:
                    f.writelines(psswordfac +'\n')
                    f.close()
                    clear()
                    break
                
                else:
                    print('Passwords do not match')
                    time.sleep(.25)
                    clear()
        print(f'The Account password set is {psswordfac}')
        time.sleep(.1)
        print(f'To change the location of this file go to {ali}/password_for_accounts.txt')
        time.sleep(.25)
        clear()
    
    #Username file
    try:
        f = open(ali + '/usernames.txt', 'r')
        f.close()
    except FileNotFoundError:
        f = open(ali + '/usernames.txt', 'x')
        f.close()
    
    #Email File
    try:
        f = open(ali + '/emails.txt', 'r')
        f.close()
    except FileNotFoundError:
        f = open(ali + '/emails.txt', 'x')
        f.close()
