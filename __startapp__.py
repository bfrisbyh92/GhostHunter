from socialrecon import reconinput
from webvuln import Webvuln
from passwordrecon import passwordrecon

cyan = "\033[1;36;40m"
green = "\033[1;32;40m"
red = "\033[1;31;40m"
Y = '\033[1;33;40m'


def Main(a):
    if (a == 1):
        reconinput()
    elif (a == 2):
        Webvuln()
    elif (a == 3):
        passwordrecon()


if __name__ == "__main__":
    print(cyan+"""
░██████╗░██╗░░██╗░█████╗░░██████╗████████╗██╗░░██╗██╗░░░██╗███╗░░██╗████████╗███████╗██████╗░
██╔════╝░██║░░██║██╔══██╗██╔════╝╚══██╔══╝██║░░██║██║░░░██║████╗░██║╚══██╔══╝██╔════╝██╔══██╗
██║░░██╗░███████║██║░░██║╚█████╗░░░░██║░░░███████║██║░░░██║██╔██╗██║░░░██║░░░█████╗░░██████╔╝
██║░░╚██╗██╔══██║██║░░██║░╚═══██╗░░░██║░░░██╔══██║██║░░░██║██║╚████║░░░██║░░░██╔══╝░░██╔══██╗
╚██████╔╝██║░░██║╚█████╔╝██████╔╝░░░██║░░░██║░░██║╚██████╔╝██║░╚███║░░░██║░░░███████╗██║░░██║
░╚═════╝░╚═╝░░╚═╝░╚════╝░╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚═════╝░╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
    """)
    print(Y)
    print(Y+"                           Github profile: https://github.com/bfrisbyh92")
    print(green+"""
                Available Modules 
           
           1.Information gathering,
           2.Web vulnerability scanning,
           3.Passwords Section
    """)
    print(Y+"Note : Type 'help' inside either module")
    a = int(input("Module >> "))
    Main(a)
