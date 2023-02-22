# Package Imports
import colorama
from colorama import Fore, Back, Style

# My Imports
from phonepasswords import phonenumwordlist
from modifywordlist import modifywordlist
from scrapwords import scrapwords

colorama.init(autoreset=True)

# Setting possible color scheme
R = Fore.RED + Style.BRIGHT
G = Fore.GREEN + Style.BRIGHT
C = Fore.CYAN + Style.BRIGHT
Y = Fore.YELLOW + Style.BRIGHT
B = Back.BLACK

# banner = '''
# ██████╗░░█████╗░░██████╗░██████╗░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░░██████╗
# ██╔══██╗██╔══██╗██╔════╝██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗██╔════╝
# ██████╔╝███████║╚█████╗░╚█████╗░░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║╚█████╗░
# ██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗░░████╔═████║░██║░░██║██╔══██╗██║░░██║░╚═══██╗
# ██║░░░░░██║░░██║██████╔╝██████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝██████╔╝
# ╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░╚═════╝░
# '''

banner2 = """
██████████████████████████████████████████████████████████
█▄─▄▄─██▀▄─██─▄▄▄▄█─▄▄▄▄█▄─█▀▀▀█─▄█─▄▄─█▄─▄▄▀█▄─▄▄▀█─▄▄▄▄█
██─▄▄▄██─▀─██▄▄▄▄─█▄▄▄▄─██─█─█─█─██─██─██─▄─▄██─██─█▄▄▄▄─█
▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▄▀
"""


def passwordrecon():
    print(B + G + banner2)
    print(B + G + """Tools available 
    
            1.Create Local Phone Number Password Lists
            2.Common Wordlist Modifications1!
            3.Scrape Websites for words
            usage : type exit to stop
            """)
    inp = input(C + B + "Info>> ")
    if inp == "1":
        phonenumwordlist()
    elif inp == "2":
        modifywordlist()
    elif inp == "3":
        scrapwords()
    elif inp == "exit":
        exit()
    elif inp == "help":
        print(G + B + """Tools available 
    
            1.PhoneNumber Password Lists
            2.Common Wordlist Modifications1!
            3.Scrape Websites for words
            usage : type exit to stop
            """)
    # elif inp == "back":
    #     Main()
    else:
        print(R + B + "Enter a valid option")


if __name__ == "__main__":
    passwordrecon()
