import os
import ctypes
import platform
import sys

def detect():
    operating_system = platform.system()
    if operating_system == "Windows":
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    else:
        return os.getuid() == 0

if not detect():
    print("This script must be run with administrative privileges. EXITING!")
    sys.exit()
else:
    print("Running with administrative privileges.")

detect()
