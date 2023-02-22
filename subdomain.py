import requests
import json
from colorama import Fore, Style, Back

cyan = Fore.CYAN + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
red = Fore.RED + Style.BRIGHT
Y = Fore.YELLOW + Style.BRIGHT 

def fuzz():
    dom = input(Back.BLACK + Fore.CYAN + "Enter Domain >> ")
    url = "https://sonar.omnisint.io/subdomains/" + dom
    r = requests.get(url)
    print(cyan + "Enumerating Subdomains ^-^ .....")
    for i in r.json():
        print(green + "[+]" + i)
    print(Y + "Subdomain Enumeration Success")

if __name__ == "__main__":
    fuzz()
