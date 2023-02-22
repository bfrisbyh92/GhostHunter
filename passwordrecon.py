
from phonepasswords import phonenumwordlist
R = '\033[1;31;40m'
G = '\033[1;32;40m'
C = '\033[1;36;40m'
Y = '\033[1;33;40m'


def passwordrecon():
    print(G+"""Tools available 
    
            1.PhoneNumber Password Lists
            
            usage : type exit to stop
            """)
    inp = (input("Info>> "))
    if (inp == '1'):
        phonenumwordlist()
    elif (inp == 'exit'):
        exit()
    elif (inp == 'help'):
        print(G+"""Tools available 
    
            1.Social media hunting using image
            
            usage : type exit to stop
            """)
    else:
        print(R+"Enter an valid option")
    while True:
        passwordrecon()


if __name__ == "__main__":
    passwordrecon()
