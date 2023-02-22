import colorama
from colorama import Back, Style

colorama.init(autoreset=True)

# Define a function to print a message with a blue background
def print_blue(msg):
    print(Back.BLUE + Style.BRIGHT + msg + Style.RESET_ALL)

def phonenumwordlist():

    # get user input for area codes
    print_blue("Enter area codes separated by commas: ")
    area_codes = input()

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


print_blue("Numbers written to numbers.txt in current directory.")
