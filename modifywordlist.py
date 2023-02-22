# Package Imports
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

# Initialize the color scheme
cyan = Fore.CYAN + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
red = Fore.RED + Style.BRIGHT
yellow = Fore.YELLOW + Style.BRIGHT


def modifywordlist():
    print("This is to modify wordlists. Some common wordlists are in all lowercase. Say you want to Uppercase the first letter, and add 1! to the end of each. Or any variety of those options. It won't harm the wordlist, you can select output in a second. Just answer a few questions and it's use will become apparent.")

    # Getting the needed User Inputs so they have control
    file_path = input(
        yellow + "Enter the file path of a word list you want to alter:")
    suffix = input(green + "Enter the suffix you want to add to each word: ")
    capitalize_index = int(
        input(cyan + "Enter the index of the character to capitalize (default is 0): ") or 0)
    output_file = input(
        red + "Enter the file path and name for the output file: ")

    # Let's open the file...
    with open(file_path, 'r') as f:
        word_list = [line.strip() for line in f]

    # Handle the business
    modified_list = []
    for word in word_list:
        modified_word = word + suffix
        if capitalize_index == 0:
            modified_word = modified_word.capitalize()
        else:
            modified_word = modified_word[:capitalize_index] + \
                modified_word[captialize_index:].capitalize()
        modified_list.append(modified_word)

    # We need to write the file, so that we keep the condition of the original wordlist.
    with open(output_file, 'w') as f:
        f.write('\n'.join(modified_list))


# Ensuring that this function only runs if it's intentionally called.
if __name__ == "__main__":
    modifywordlist()
