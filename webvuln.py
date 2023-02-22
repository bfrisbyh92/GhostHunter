# from clickjack import ClickJacking
# from hostheader import HostHeader
# from subdomain import fuzz
# from reverseip import ReverseIP
# cyan = "\033[1;36;40m"
# green = "\033[1;32;40m"
# red = "\033[1;31;40m"
# Y = '\033[1;33;40m'


# def Webvuln():
#     print(green+"""
#                1.ClickJacking,
#                2.Host header injection.
#                3.Subdomain Enumeration.
#                4.Reverse IP
#                """)
#     inp = (input("Vulnerability >> "))
#     if (inp == '1'):
#         ClickJacking()
#     elif (inp == '2'):
#         HostHeader()
#     elif (inp == '3'):
#         fuzz()
#     elif (inp == '4'):
#         ReverseIP()
#     elif (inp == 'help'):
#         print(green+"""
#                1.ClickJacking,
#                2.Host header injection.
#                3.Subdomain Enumeration.
#                4.Reverse IP
#                """)
#     else:
#         print(red+"Invalid choice")
#     while True:
#         Webvuln()


# if __name__ == "__main__":
#     Webvuln()

from clickjack import ClickJacking
from hostheader import HostHeader
from subdomain import fuzz
from reverseip import ReverseIP
cyan = "\033[1;36;40m"
green = "\033[1;32;40m"
red = "\033[1;31;40m"
Y = '\033[1;33;40m'
BG_YELLOW = '\033[43m'
BLACK = '\033[30m'
RESET = '\033[0m'


def Webvuln():
    print(BG_YELLOW + BLACK + """
               1.ClickJacking,
               2.Host header injection.
               3.Subdomain Enumeration.
               4.Reverse IP
               """ + RESET)
    inp = (input("Vulnerability >> "))
    if (inp == '1'):
        ClickJacking()
    elif (inp == '2'):
        HostHeader()
    elif (inp == '3'):
        fuzz()
    elif (inp == '4'):
        ReverseIP()
    elif (inp == 'help'):
        print(BG_YELLOW + BLACK + """
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
