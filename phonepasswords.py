import colorama
from colorama import Fore, Style,Back

colorama.init(autoreset=True)

cyan = Fore.CYAN + Style.BRIGHT
G = Fore.GREEN + Style.BRIGHT
B = Back.BLACK

# Define a function to print a message with a blue background
def print_blue():
    print(cyan + "This is a tool to create wordlists from your local area codes. Keep in mind more than one area code at a time is a pretty large file. One is about the size of rockyou.", Style.RESET_ALL)
    print(cyan + "The output will be in the current directory.")
    print(cyan + "I find these lists best fit for WiFi Passwords.")
        
def phonenumwordlist():
    # get user input for area codes
    print_blue()
    area_codes = input( B + G + "Enter area codes separated by commas: ")

    # split area codes into a list
    area_codes = [code.strip() for code in area_codes.split(',')]

    # generate a list of phone numbers for each area code
    phone_numbers = []
    for code in area_codes:
        for i in range(10**7, 10**8):
            phone_numbers.append(code + str(i))

    # write phone numbers to a file
    with open("numbers.txt", "w") as file:
        for number in phone_numbers:
            file.write(number + "\n")

    print_blue()
    print(cyan + "Numbers written to numbers.txt in current directory." + Style.RESET_ALL)

if __name__ == "__main__":
    phonenumwordlist()
