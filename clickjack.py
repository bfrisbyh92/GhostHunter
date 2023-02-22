import colorama
from colorama import Fore, Back, Style

from urllib.request import urlopen

colorama.init(autoreset=True)


def ClickJacking():
    host = input(Back.BLACK + Fore.CYAN + "Enter host >> ")
    port = int(input(Back.BLACK + Fore.CYAN + "Enter port >> "))

    if port == 80:
        port = 'http://'
    elif port == 443:
        port = 'https://'
    else:
        print(Fore.RED + "Couldn't fetch data for the given PORT")
        return

    url = (port + host)

    data = urlopen(url)
    headers = data.info()

    if not "X-Frame-Options" in headers:
        print(Fore.GREEN + "Website is vulnerable to ClickJacking")
    else:
        print(Fore.RED + "Website is not Vulnerable to ClickJacking")


if __name__ == "__main__":
    ClickJacking()
