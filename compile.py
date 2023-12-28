#!/usr/bin/env python3
import os
import time
os.system("sudo apt install git")
os.system("git clone https://github.com/htr-tech/zphisher.git")
os.system("sudo apt install npm")
time.sleep(1)
print("importing modules..")
os.system('pip install -r requirements.txt')
