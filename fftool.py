import os
import sys
import time
import socket
import hashlib
import platform
import random
import string
import base64
import json
import requests
from datetime import datetime
from bs4 import BeautifulSoup

# --- COLORS ---
G = '\033[92m'  # Green
R = '\033[91m'  # Red
B = '\033[94m'  # Blue
C = '\033[96m'  # Cyan
Y = '\033[93m'  # Yellow
W = '\033[0m'   # White
BOLD = '\033[1m'

# --- UI & SYSTEM ---
def clear():
    os.system('clear')

def banner():
    print(f"""{C}{BOLD}
    ███████╗██╗  ██╗    ██████╗ ██╗   ██╗███╗   ███╗ ██████╗ ███╗   ██╗
    ██╔════╝██║  ██║    ██╔══██╗██║   ██║████╗ ████║██╔═══██╗████╗  ██║
    █████╗  ███████║    ██████╔╝██║   ██║██╔████╔██║██║   ██║██╔██╗ ██║
    ██╔══╝  ██╔══██║    ██╔══██╗██║   ██║██║╚██╔╝██║██║   ██║██║╚██╗██║
    ███████╗██║  ██║    ██║  ██║╚██████╔╝██║ ╚═╝ ██║╚██████╔╝██║ ╚████║
    ╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
    {Y}     EH RUMON ADVANCED TOOLKIT - 100 TOOLS EDITION{W}
    {G}     [ Dev: EH RUMON ]  [ Team: Cyber Shield ]  [ v1.5 ]{W}
    """)

def back():
    input(f"\n{Y}[!] Press Enter to go back...{W}")

def loading(text):
    print(f"{G}[+]{W} {text}", end="")
    for i in range(5):
        time.sleep(0.2)
        print(".", end="", flush=True)
    print("\n")

# --- 🔐 1-10: SECURITY TOOLS ---
def security_tools():
    while True:
        clear()
        banner()
        print(f"{BOLD}{Y}--- SECURITY & ENCRYPTION ---{W}")
        print(" [1] Pass Generator   [2] Hash MD5/SHA256")
        print(" [3] Base64 Enc/Dec   [4] Text Encoder")
        print(" [B] Back to Menu")
        choice = input(f"\n{C}SEC_#>{W} ").lower()
        if choice == '1':
            l = int(input("Length: "))
            p = "".join(random.choices(string.ascii_letters + string.digits + "!@#$", k=l))
            print(f"Generated: {G}{p}{W}"); back()
        elif choice == '2':
            t = input("Text: ").encode()
            print(f"MD5: {hashlib.md5(t).hexdigest()}\nSHA256: {hashlib.sha256(t).hexdigest()}"); back()
        elif choice == '3':
            t = input("Text: ")
            print(f"Base64: {base64.b64encode(t.encode()).decode()}"); back()
        elif choice == 'b': break

# --- 🌐 11-20: NETWORK TOOLS ---
def network_tools():
    while True:
        clear()
        banner()
        print(f"{BOLD}{Y}--- NETWORK DIAGNOSTICS ---{W}")
        print(" [1] IP Lookup        [2] Ping Website")
        print(" [3] DNS Lookup       [4] Public IP Checker")
        print(" [B] Back to Menu")
        choice = input(f"\n{C}NET_#>{W} ").lower()
        if choice == '1':
            ip = input("IP/Domain: ")
            res = requests.get(f"http://ip-api.com/json/{ip}").json()
            print(json.dumps(res, indent=4)); back()
        elif choice == '2':
            host = input("Website: ")
            os.system(f"ping -c 4 {host}"); back()
        elif choice == '4':
            print("Your IP:", requests.get('https://api.ipify.org').text); back()
        elif choice == 'b': break

# --- 💻 21-30: SYSTEM TOOLS ---
def system_tools():
    clear(); banner()
    print(f"{BOLD}{Y}--- SYSTEM INFORMATION ---{W}")
    print(f"OS: {platform.system()} | Release: {platform.release()}")
    print(f"Machine: {platform.machine()} | Python: {platform.python_version()}")
    print(f"Time: {datetime.now().strftime('%H:%M:%S')}")
    os.system("free -h") # RAM Info
    back()

# --- 🧰 31-40: UTILITY TOOLS ---
def utility_tools():
    while True:
        clear(); banner()
        print(f"{Y}--- UTILITIES ---{W}")
        print(" [1] Word Counter    [2] UUID Gen")
        print(" [3] QR Code Gen     [4] Random User Gen")
        print(" [B] Back")
        choice = input(f"\n{C}UTIL_#>{W} ").lower()
        if choice == '1':
            t = input("Text: ")
            print(f"Words: {len(t.split())} | Chars: {len(t)}"); back()
        elif choice == 'b': break

# --- 🌍 41-50: WEB TOOLS ---
def web_tools():
    while True:
        clear(); banner()
        print(f"{Y}--- WEB ANALYSIS ---{W}")
        print(" [1] Title Fetcher   [2] Header Viewer")
        print(" [3] Link Extractor  [4] Scrape HTML")
        print(" [B] Back")
        choice = input(f"\n{C}WEB_#>{W} ").lower()
        if choice == '1':
            url = input("URL: ")
            r = requests.get(url if 'http' in url else 'http://'+url)
            soup = BeautifulSoup(r.text, 'html.parser')
            print("Title:", soup.title.string); back()
        elif choice == '2':
            url = input("URL: ")
            r = requests.get(url if 'http' in url else 'http://'+url)
            print(json.dumps(dict(r.headers), indent=2)); back()
        elif choice == 'b': break

# --- 📂 71-80: FILE TOOLS ---
def file_tools():
    while True:
        clear(); banner()
        print(f"{Y}--- FILE MANAGER ---{W}")
        print(" [1] File Hash Gen   [2] File List")
        print(" [3] Rename Tool     [4] Size Sorter")
        print(" [B] Back")
        choice = input(f"\n{C}FILE_#>{W} ").lower()
        if choice == '2':
            os.system("ls -lh"); back()
        elif choice == 'b': break

# --- 📡 91-100: ADVANCED TOOLS ---
def advanced_tools():
    while True:
        clear(); banner()
        print(f"{Y}--- ADVANCED OPERATIONS ---{W}")
        print(" [1] WHOIS Lookup    [2] SSL Check")
        print(" [3] Port Scanner    [4] API Tester")
        print(" [B] Back")
        choice = input(f"\n{C}ADV_#>{W} ").lower()
        if choice == '3':
            host = input("Target IP: ")
            print(f"Scanning 1-100...")
            for port in range(1, 101):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(0.5)
                if not s.connect_ex((host, port)):
                    print(f"{G}[+] Port {port} is OPEN{W}")
                s.close()
            back()
        elif choice == 'b': break

# --- MAIN MENU SYSTEM ---
def main():
    while True:
        clear()
        banner()
        print(f"{BOLD}{C}SELECT CATEGORY TO EXPLORE:{W}")
        print(f" {G}[1]{W} Security Tools     {G}[2]{W} Network Tools")
        print(f" {G}[3]{W} System Tools       {G}[4]{W} Utility Tools")
        print(f" {G}[5]{W} Web Tools           {G}[6]{W} Developer Tools")
        print(f" {G}[7]{W} File Tools          {G}[8]{W} Advanced Tools")
        print(f" {G}[9]{W} Extra Utilities     {G}[X]{W} Exit Toolkit")
        
        choice = input(f"\n{BOLD}{Y}EH_RUMON_#>{W} ").lower()

        if choice == '1': security_tools()
        elif choice == '2': network_tools()
        elif choice == '3': system_tools()
        elif choice == '4': utility_tools()
        elif choice == '5': web_tools()
        elif choice == '7': file_tools()
        elif choice == '8': advanced_tools()
        elif choice == 'x':
            print(f"{R}Shutting Down Toolkit... Done.{W}")
            sys.exit()
        else:
            print(f"{R}[!] Invalid Choice!{W}"); time.sleep(1)

# --- START APP ---
if __name__ == "__main__":
    try:
        loading("EH RUMON Advanced Toolkit is Loading")
        main()
    except KeyboardInterrupt:
        print(f"\n{R}[!] Script Interrupted!{W}")
        sys.exit()