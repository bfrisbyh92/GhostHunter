import requests
from colorama import Fore, Style, Back

cyan = Fore.CYAN + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
red = Fore.RED + Style.BRIGHT
yellow = Fore.YELLOW + Style.BRIGHT


def HostHeader():
    host = input("Enter host >> ")
    port = int(input("Enter port >> "))

    if port == 80:
        port = 'http://'
    elif port == 443:
        port = 'https://'
    else:
        print(red + "Could not fetch data for the given PORT")

    url = (port + host)
    headers = {'Host': 'http://evil.com'}
    response = requests.get(url, headers=headers)

    if 'evil.com' in response.headers:
        print(green + "Vulnerable to Host Header Injection")
    else:
        print(Back.RED + Fore.BLACK + Style.NORMAL +
              "NOT VULNERABLE TO HOST HEADER INJECTION")


if __name__ == "__main__":
    HostHeader()
