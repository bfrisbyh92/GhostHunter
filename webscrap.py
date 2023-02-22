import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style, Back


def Links():
    print(Fore.CYAN + Back.BLACK + "Note : http://example.com")
    url = input(Fore.GREEN + Back.BLACK + "Enter the URL (http:// >> ")
    print('')
    print(Fore.GREEN + Back.BLACK + "[+] Fetching links.....")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for link in soup.find_all('a'):
        lin = link.get('href')
        if (lin.startswith('http')):
            print(Fore.CYAN + Back.BLACK + "[+] ", lin)
    print(Fore.GREEN + Back.BLACK + "Fetched Successfully...")


if __name__ == "__main__":
    Links()
