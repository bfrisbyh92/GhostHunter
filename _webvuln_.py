from clickjack import ClickJacking
from hostheader import HostHeader
from subdomain import fuzz
from reverseip import ReverseIP
from colorama import Fore, Back, Style, init

init()

cyan = Fore.CYAN
green = Fore.GREEN
red = Fore.RED
Y = Fore.YELLOW
BG_YELLOW = Back.YELLOW
BLACK = Fore.BLACK + Back.RESET
RESET = Style.RESET_ALL

banner2 = f'''
{cyan}
╦ ╦╔═╗╔╗   ╦  ╦╦ ╦╦  ╔╗╔╔═╗
║║║║╣ ╠╩╗  ╚╗╔╝║ ║║  ║║║╚═╗
╚╩╝╚═╝╚═╝   ╚╝ ╚═╝╩═╝╝╚╝╚═╝
'''


def Webvuln():
    print(cyan + banner2)
    print(green + """
               1.ClickJacking,
               2.Host header injection.
               3.Subdomain Enumeration.
               4.Reverse IP
               """ + RESET)
    inp = (input(Fore.LIGHTYELLOW_EX + Back.BLACK + "Vulnerability >> "))
    if (inp == '1'):
        ClickJacking()
    elif (inp == '2'):
        HostHeader()
    elif (inp == '3'):
        fuzz()
    elif (inp == '4'):
        ReverseIP()
    elif (inp == 'help'):
        print(cyan + """
               1.ClickJacking,
               2.Host header injection.
               3.Subdomain Enumeration.
               4.Reverse IP
               """ + RESET)
    else:
        print(red+BLACK+"Invalid choice"+RESET)
    while True:
        Webvuln()


if __name__ == "__main__":
    Webvuln()
