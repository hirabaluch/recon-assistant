from colorama import Fore

def info(msg):
    print(Fore.CYAN + "[*] " + msg)

def good(msg):
    print(Fore.GREEN + "[+] " + msg)

def bad(msg):
    print(Fore.RED + "[-] " + msg)
