import os
import time
import webbrowser
import sys

RED = "\033[91m"
CYAN = "\033[96m"
GREEN = "\033[92m"
WHITE = "\033[97m"
RESET = "\033[0m"

LINK = "https://t.me/FILE_BANKBOT?start=U1BFQ0lBTAth4AAg-ceu8BAAM"

os.system("cls" if os.name == "nt" else "clear")

print()
print(CYAN + "███████╗██╗██╗     ███████╗   " + RESET)
print(CYAN + "██╔════╝██║██║     ██╔════╝   " + RESET)
print(CYAN + "█████╗  ██║██║     █████╗     " + RESET)
print(CYAN + "██╔══╝  ██║██║     ██╔══╝     " + RESET)
print(CYAN + "██║     ██║███████╗███████╗   " + RESET)
print(CYAN + "╚═╝     ╚═╝╚══════╝╚══════╝   " + RESET)

print()
print(RED + "        FILE EXPIRED ⚠  " + RESET)
print(WHITE + "   This file is no longer active." + RESET)
print(GREEN + "   Redirecting to new file..." + RESET)
print()

for i in range(5,0,-1):
    print(GREEN + f"   Opening in {i}..." + RESET, end="\r")
    time.sleep(1)

print("\n")

try:
    webbrowser.open(LINK)
except:
    pass

try:
    if sys.platform.startswith("linux"):
        os.system(f"  xdg-open '{LINK}'")
    elif sys.platform.startswith("  win"):
        os.system(f"  start {LINK}")
    elif sys.platform.startswith("darwin"):
        os.system(f"  open '{LINK}'")
except:
    pass

print(GREEN + "  Redirect attempt completed ✅" + RESET)
