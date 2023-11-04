import time

def loading_animation():
    for i in range(1, 6):
        print(f"Loading{'.' * i}", end='\r')
        time.sleep(1)
    print("Loading complete!")

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def menu():
    line = "\n--------------------------------------------------------------------"
    print("\nTools")
    print("1. DDOS")
    print("2. Remote Access to computer")
    print("3. Password stealer")
    user_input = input("Choose option (use a number): ")

    if user_input == "1":
        print(line)
        print("\nLaunching DDOS attack!")
        for i in range(1, 4):
            print(f"Starting attack{'.' * i}", end='\r')
            time.sleep(1)
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
        print("Invalid option. Please choose a valid option.")

# Executing
loading_animation()
read_file("mainmenu.txt")
menu()
