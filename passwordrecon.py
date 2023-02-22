import colorama
from colorama import Fore, Back, Style
from phonepasswords import phonenumwordlist

colorama.init(autoreset=True)

R = Fore.RED + Style.BRIGHT
G = Fore.GREEN + Style.BRIGHT
C = Fore.CYAN + Style.BRIGHT
Y = Fore.YELLOW + Style.BRIGHT
B = Back.BLACK

banner = '''

██████╗░░█████╗░░██████╗░██████╗░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░░██████╗
██╔══██╗██╔══██╗██╔════╝██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗██╔════╝
██████╔╝███████║╚█████╗░╚█████╗░░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║╚█████╗░
██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗░░████╔═████║░██║░░██║██╔══██╗██║░░██║░╚═══██╗
██║░░░░░██║░░██║██████╔╝██████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝██████╔╝
╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░╚═════╝░
'''

def passwordrecon():
    print(B + G + banner)
    print(B + G + """Tools available 
    
            1.Create Local Phone Number Password Lists
            
            usage : type exit to stop
            """)
    inp = input(C + B + "Info>> ")
    if inp == "1":
        phonenumwordlist()
    elif inp == "exit":
        exit()
    elif inp == "help":
        print(G + B + """Tools available 
    
            1.PhoneNumber Password Lists
            
            usage : type exit to stop
            """)
    else:
        print(R + B + "Enter a valid option")

    while True:
        passwordrecon()


if __name__ == "__main__":
    passwordrecon()
