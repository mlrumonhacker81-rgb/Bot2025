import os
import time
import sys

name = "EH RUMON"
title = "TERMUX PYTHON TOOL"

colors = [
"\033[91m",
"\033[92m",
"\033[93m",
"\033[94m",
"\033[95m",
"\033[96m"
]

def clear():
    os.system("clear")

def loading():
    clear()
    print("\033[92mLoading Tool...\033[0m")
    for i in range(20):
        sys.stdout.write("█")
        sys.stdout.flush()
        time.sleep(0.1)
    time.sleep(1)

def banner():
    for c in colors:
        clear()
        print(c)
        print("====================================")
        print("           EH RUMON")
        print("====================================")
        print("        TERMUX PYTHON TOOL")
        print("\033[0m")
        time.sleep(0.2)

def menu():
    print("\033[96m")
    print("1. Tool Information")
    print("2. My Contact")
    print("3. System Info")
    print("4. Exit")
    print("\033[0m")

loading()
banner()

while True:
    menu()
    choice = input("Select Option : ")

    if choice == "1":
        print("\nThis tool created by EH RUMON\n")

    elif choice == "2":
        print("\nTelegram : @yourusername\n")

    elif choice == "3":
        os.system("uname -a")

    elif choice == "4":
        print("Good Bye...")
        break

    else:
        print("Invalid Option")