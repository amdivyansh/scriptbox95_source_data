from colorama import Fore
import os
import time
from dta import *
os.system('cls||clear')
def load():
    os.system('cls||clear')
    print("Loading [1%]")
    time.sleep(2)
    os.system('cls||clear')
    print("Loading [100%]")
    os.system('cls||clear')
    print(go)
    i = 0
    while i < 10:
        print(con+"Select An Option For Your Victim")
        print(lts)
        user_input = int(input(con+"Enter your option:"))
        if user_input < 1 or user_input > 10:
            print("The number you entered is not valid. Try again")
            pass
        if user_input == 1:
            zphisher()
        if user_input == 2:
            truecallerjs()
        else:
            i += 1
            print('pass')



def zphisher():
    os.system('cls||clear')
    os.system("bash ./zphisher/zphisher.sh")
def truecallerjs():
    os.system('cls||clear')
    os.system("npm install -g truecallerjs")







load()