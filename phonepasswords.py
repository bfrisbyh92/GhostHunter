def phonenumwordlist():

    # get user input for area codes
    area_codes = input("Enter area codes separated by commas: ")

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


print("Numbers written to numbers.txt in current directory.")
