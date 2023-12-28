#!/usr/bin/env python3
from colorama import Fore
import os
import time
import sys
from dta import *
os.system('cls||clear')

def load():
    os.system('cls||clear')
    print(con_inf+"Loading [1%]")
    time.sleep(2)
    os.system('cls||clear')
    print(con_inf+"Loading [10%]")
    time.sleep(1)
    os.system('cls||clear')
    print(con_inf+"Loading [35%]")
    time.sleep(0.5)
    os.system('cls||clear')
    print(con_inf+"Loading [40%]")
    time.sleep(0.5)
    os.system('cls||clear')
    print(con_inf+"Loading [56%]")
    time.sleep(0.5)
    os.system('cls||clear')
    print(con_inf+"Loading [61%]")
    time.sleep(0.5)
    os.system('cls||clear')
    print(con_inf+"Loading [79%]")
    time.sleep(0.5)
    os.system('cls||clear')
    print(con_inf+"Loading [91%]")
    time.sleep(0.5)
    os.system('cls||clear')
    print(con_inf+"Loading [100%]")
    time.sleep(2)
    os.system('cls||clear')
    print(go)
    i = 0
    while i < 10:
        print(con_pls+"Select An Option For Your Victim")
        print(lts)
        user_input = int(input(con+"Enter your option:"))
        if user_input < 1 or user_input > 2:
            print(con_inf+"The number you entered is not valid. Try again")
        if user_input == 1:
            zphisher()
        if user_input == 2:
            truecallerjs()
        



def truecallerjs():
    process = os.popen("truecallerjs")
    is_installed = process.read()
    process.close()

# If it is installed, stop the script
    if "truecallerjs" in is_installed:
        print("truecallerjs is already installed.")
        os.system("truecallerjs")
        npm2 = input(con+"truecallerjs")
        os.system("truecallerjs "+npm2)
    else:
    # Install truecallerjs
        os.system("sudo npm install -g truecallerjs")
        print("truecallerjs has been installed.")
        os.system('cls||clear')
        os.system("truecallerjs ")
        npm = input(con+"truecallerjs ")
        os.system("truecallerjs "+npm)
def zphisher():
    os.system('cls||clear')
    os.system("bash ./zphisher/zphisher.sh")







load()
