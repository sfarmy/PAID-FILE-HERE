import os
import time
import webbrowser

RED = "\033[91m"
CYAN = "\033[96m"
GREEN = "\033[92m"
WHITE = "\033[97m"
RESET = "\033[0m"

os.system("cls" if os.name == "nt" else "clear")

print()
print(CYAN + "███████╗██╗██╗     ███████╗   " + RESET)
print(CYAN + "██╔════╝██║██║     ██╔════╝    " + RESET)
print(CYAN + "█████╗  ██║██║     █████╗       " + RESET)
print(CYAN + "██╔══╝  ██║██║     ██╔══╝      " + RESET)
print(CYAN + "██║     ██║███████╗███████╗    " + RESET)
print(CYAN + "╚═╝     ╚═╝╚══════╝╚══════╝     " + RESET)
print()
print(RED + "        FILE EXPIRED ⚠    " + RESET)
print(WHITE + "   This file is no longer active." + RESET)
print(GREEN + "   Redirecting to new file in 5 seconds..." + RESET)
print()

for i in range(5, 0, -1):
    print(GREEN + f"   Opening in {i}..." + RESET, end="\r")
    time.sleep(1)
    
webbrowser.open("https://t.me/FILE_BANKBOT?start=U1BFQ0lBTASR4AAg-ceu8BAAM")

print("\n   Done ✅")
