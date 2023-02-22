import requests
import time
from datetime import datetime
from colorama import Fore, Style, Back

cyan = Fore.CYAN + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
red = Fore.RED + Style.BRIGHT
Y = Fore.YELLOW + Style.BRIGHT


def urlinfo():
    print(Y + Back.BLACK + "Note : URL = http://example.com")
    url = input(green + Back.BLACK + "URL >> ")
    print("-"*50)
    print(cyan+"          Trace Results        ")
    print("-"*50)
    try:
        r = requests.get(url)
        print()
        current_datetime = datetime.now()
        print(green + "[+]Traced Date and Time :", current_datetime)
        print(green+"[-]"+"301 Redirected")
        print(cyan+"[-]"+r.url)
    except Exception as e:
        print(red+"Error Occured :", e)


if __name__ == "__main__":
    urlinfo()
