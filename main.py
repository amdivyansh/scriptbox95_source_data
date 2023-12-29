#!/usr/bin/env python3
from colorama import Fore
import os
import time
from time import sleep
import sys
from dta import *
os.system('clear')

import sys
from time import sleep
def handle_user_input():
    while True:
        try:
            print(con+"Select An Option For Your Victim")
            print(lts)
            user_option = int(input(con_pls+"Enter your option:"))
            return user_option
        except ValueError:
            print(con_inf+"Error: Please enter an integer.")
            time.sleep(2)
            main()
            """sys.exit(1)"""
        except KeyboardInterrupt:
            print('\n'+con_inf+"Exiting ..!!!")
            sleep(2)
            sys.exit()

def main():
    os.system('clear')
    print(go)
    user_input = handle_user_input()
    try:
        if user_input < 1 or user_input > 2:
            print(con_inf+"The number you entered is not valid. Try again")
            time.sleep(2)
            main()
        elif user_input == 1:
            zphisher()
        elif user_input == 2:
            truecallerjs()
    except KeyboardInterrupt:
            print('\n'+con_inf+"Exiting ..!!!")
            sleep(2)
            sys.exit()

def load():
    os.system('clear')
    print(con_inf+"Loading [1%]")
    time.sleep(2)
    os.system('clear')
    print(con_inf+"Loading [10%]")
    time.sleep(1)
    os.system('clear')
    print(con_inf+"Loading [35%]")
    time.sleep(0.5)
    os.system('clear')
    print(con_inf+"Loading [40%]")
    time.sleep(0.5)
    os.system('clear')
    print(con_inf+"Loading [56%]")
    time.sleep(0.5)
    os.system('clear')
    print(con_inf+"Loading [61%]")
    time.sleep(0.5)
    os.system('clear')
    print(con_inf+"Loading [79%]")
    time.sleep(0.5)
    os.system('clear')
    print(con_inf+"Loading [91%]")
    time.sleep(0.5)
    os.system('clear')
    print(con_inf+"Loading [100%]")
    time.sleep(2)
    os.system('clear')
    main()


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
        os.system('clear')
        os.system("truecallerjs ")
        npm = input(con+"truecallerjs ")
        os.system("truecallerjs "+npm)
def zphisher():
    os.system('clear')
    os.system("bash ./zphisher/zphisher.sh")







load()
