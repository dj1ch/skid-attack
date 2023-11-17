import time
import sys
# my own libraries
import ddos
import access
import password
import detect

# variables
line = "\n--------------------------------------------------------------------"

# functions
def loading_animation():
    detect.detect()
    for i in range(1, 6):
        print(f"\nLoading{'.' * i}", end='\r')
        time.sleep(1)
    print("Loading complete!")

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        print("Even if the file is not found, the script may still be able to run")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Even if the file is not found, the script may still be able to run")

def menu():
    print("\033[1m\nTools\033[0m")
    print("\033[1m[1.] DDOS\033[0m")
    print("\033[1m[2.] Remote Access to computer\033[0m")
    print("\033[1m[3.] Password stealer\033[0m")

def attack():
    user_input = input("Choose option (use a number): ")
    if user_input == "1":
        print(line)
        print("\nLaunching DDOS attack!")
        ddos.start()
        ddos.attack()
        print(" " * 20)
        print("Attack finished!")
        print(line)

    elif user_input == "2":
        print(line)
        print("\nInitiating remote access")
        for i in range(1, 4):
            print(f"Starting attack{'.' * i}", end='\r')
            time.sleep(1)
        print(" " * 20)
        print("Attack finished!")
        print(line)

    elif user_input == "3":
        print(line)
        print("\nStealing passwords")
        for i in range(1, 4):
            print(f"Starting attack{'.' * i}", end='\r')
            time.sleep(1)
        print(" " * 20)
        print("Attack finished!")
        print(line)

    else:
        print("Invalid option, choose a number. EXITTING!")
        sys.exit()

# Executing
loading_animation()
read_file("mainmenu.txt")
menu()
attack()
