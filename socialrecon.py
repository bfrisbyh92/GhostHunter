import time
import sys
import colorama
from colorama import Fore, Back, Style
from url import urlinfo
from pdfanalysis import pdfinfo
from imagerecon import recon
from iplocator import iplocate
from TraceIP import read_multiple_ip
from webscrap import Links
from NameInfo import Nameinfo
from number import number

colorama.init(autoreset=True)

R = Fore.BLACK + Back.BLUE + Style.BRIGHT
G = Fore.BLACK + Back.BLUE + Style.BRIGHT
C = Fore.BLACK + Back.BLUE + Style.BRIGHT
Y = Fore.BLACK + Back.BLUE + Style.BRIGHT
B = Back.BLUE + Style.BRIGHT

def reconinput():
    print(G + B + """Tools available 

            1.Social media hunting using image
            2.Trace Single IP
            3.Heatmap
            4.URL redirection checker
            5.PDF meta data analysis
            6.URL lookup in webpages
            usage : type exit to stop
            """)
    inp = input(C + B + "Info>> ")
    if inp == "1":
        recon()
    elif inp == "2":
        iplocate()
    elif inp == "3":
        read_multiple_ip()
    elif inp == "4":
        urlinfo()
    elif inp == "5":
        pdfinfo()
    elif inp == "6":
        Links()
    elif inp == "exit":
        exit()
    elif inp == "help":
        print(G + B + """Tools available 

            1.Social media hunting using image
            2.Trace Single IP
            3.Heatmap
            4.URL redirection checker
            5.PDF meta data analysis
            6.URL lookup in webpages
            usage : type exit to stop
            """)
    else:
        print(R + B + "Enter a valid option")
    while True:
        reconinput()


if __name__ == "__main__":
    reconinput()
