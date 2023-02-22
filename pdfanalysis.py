import colorama
from colorama import Fore, Style
from PyPDF2 import PdfFileReader

colorama.init(autoreset=True)

R = Fore.RED + Style.BRIGHT
G = Fore.GREEN + Style.BRIGHT
C = Fore.CYAN + Style.BRIGHT
Y = Fore.YELLOW + Style.BRIGHT


def pdfinfo():
    filep = input("File path >> ")
    with open(filep, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()
    try:
        author = info.author
        creator = info.creator
        producer = info.producer
        print(C+"[+] Author        : ", author)
        print(C+"[+] Creator       : ", creator)
        print(C+"[+] Producer      : ", producer)
        cdate = info['/CreationDate']
        cyear = cdate[2:6]
        cmonth = cdate[6:8]
        cd = cdate[8:10]
        print(C+"[+] Creation Date : ", cd, ":", cmonth, ":", cyear)
        mdate = info['/ModDate']
        myear = cdate[2:6]
        mmonth = cdate[6:8]
        md = cdate[8:10]
        print(C+"[+] Modified Date : ", md, ":", mmonth, ":", myear)
    except:
        print(R+"[-] Meta data not available")


if __name__ == "__main__":
    pdfinfo()
