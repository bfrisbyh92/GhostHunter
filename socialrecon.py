import time
import sys
from url import urlinfo
from pdfanalysis import pdfinfo
from imagerecon import recon
from iplocator import iplocate
from TraceIP import read_multiple_ip
from webscrap import Links
from NameInfo import Nameinfo
from number import number
R = '\033[1;31;40m'
G = '\033[1;32;40m'
C = '\033[1;36;40m'
Y = '\033[1;33;40m'


def reconinput():
    print(G+"""Tools available 
    
            1.Social media hunting using image
            2.Trace Single IP
            3.Heatmap
            4.URL redirection checker
            
            usage : type exit to stop
            """)
    inp = (input("Info>> "))
    if (inp == '1'):
        recon()
    elif (inp == '2'):
        iplocate()
    elif (inp == '3'):
        read_multiple_ip()
    elif (inp == '4'):
        urlinfo()
    elif (inp == 'exit'):
        exit()
    elif (inp == 'help'):
        print(G+"""Tools available 
    
            1.Social media hunting using image
            2.Trace Single IP
            3.Heatmap
            4.URL redirection checker
            
            usage : type exit to stop
            """)
    else:
        print(R+"Enter an valid option")
    while True:
        reconinput()


if __name__ == "__main__":
    reconinput()
