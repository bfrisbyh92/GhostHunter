### Package Imports
import colorama
from colorama import Fore, Back, Style

### My Imports
from _osint_ import reconinput
from _webvuln_ import Webvuln
from _passwords_ import passwordrecon

colorama.init(autoreset=True)

cyan = Fore.CYAN + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
red = Fore.RED + Style.BRIGHT
yellow = Fore.YELLOW + Style.BRIGHT


def Main(a):
    if (a == 1):
        reconinput()
    elif (a == 2):
        Webvuln()
    elif (a == 3):
        passwordrecon()


if __name__ == "__main__":
    print(cyan+"")
    print(cyan+"░██████╗░██╗░░██╗░█████╗░░██████╗████████╗██╗░░██╗██╗░░░██╗███╗░░██╗████████╗███████╗██████╗░")
    print(cyan+"██╔════╝░██║░░██║██╔══██╗██╔════╝╚══██╔══╝██║░░██║██║░░░██║████╗░██║╚══██╔══╝██╔════╝██╔══██╗")
    print(cyan+"██║░░██╗░███████║██║░░██║╚█████╗░░░░██║░░░███████║██║░░░██║██╔██╗██║░░░██║░░░█████╗░░██████╔╝")
    print(cyan+"██║░░╚██╗██╔══██║██║░░██║░╚═══██╗░░░██║░░░██╔══██║██║░░░██║██║╚████║░░░██║░░░██╔══╝░░██╔══██╗")
    print(cyan+"╚██████╔╝██║░░██║╚█████╔╝██████╔╝░░░██║░░░██║░░██║╚██████╔╝██║░╚███║░░░██║░░░███████╗██║░░██║")
    print(cyan+"░╚═════╝░╚═╝░░╚═╝░╚════╝░╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚═════╝░╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝")
    print(yellow+"Github profile: https://github.com/bfrisbyh92")
    print(green+"")
    print(green+"Available Modules")
    print(green+"")
    print(green+"1. Information gathering")
    print(green+"2. Web vulnerability scanning")
    print(green+"3. Passwords Section")
    print(yellow+"")
    print(yellow+"Note: Type 'help' inside either module. For now, select an option.")
    a = int(input("Module >> "))
    Main(a)
