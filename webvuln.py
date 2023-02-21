from clickjack import ClickJacking
from hostheader import HostHeader
from subdomain import fuzz
from reverseip import ReverseIP
cyan = "\033[1;36;40m"
green = "\033[1;32;40m"
red = "\033[1;31;40m"
Y = '\033[1;33;40m'


def Webvuln():
    print(green+"""
               1.ClickJacking,
               2.Host header injection.
               """)
    inp = (input("Vulnerability >> "))
    if (inp == '1'):
        ClickJacking()
    elif (inp == '2'):
        HostHeader()

    elif (inp == 'help'):
        print(green+"""
               1.ClickJacking,
               2.Host header injection.
               """)
    else:
        print(red+"Invalid choice")
    while True:
        Webvuln()


if __name__ == "__main__":
    Webvuln()
