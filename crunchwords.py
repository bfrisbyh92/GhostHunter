import re
from colorama import Fore, Back, Style

import re


def generate_words():
    input_file = input("File of words we will crunch and change up:")
    # Read in words from input file
    with open(input_file, 'r') as f:
        words = f.read().splitlines()

    # Get user input for capitalization and character addition
    first_letter_cap = input(
        'Do you want the first letter of each word capitalized? (y/n): ').lower() == 'y'
    add_chars = input(
        'Do you want to add characters to the end of each word? (y/n): ').lower() == 'y'

    # Generate all possible word combinations
    if first_letter_cap:
        words = [word.capitalize() for word in words]
    if add_chars:
        chars = input('Enter the characters to add to the end of each word: ')
        words = [word + char for word in words for char in chars]
    all_combinations = []
    for i in range(1, len(words)+1):
        for j in range(len(words)-i+1):
            combination = words[j]
            for k in range(1, i):
                combination += words[j+k]
            all_combinations.append(combination)

    # Write all combinations to file
    output_file = input('Enter the output file name: ')
    with open(output_file, 'w') as f:
        f.write('\n'.join(all_combinations))

    print(f'Generated {len(all_combinations)} combinations.')


if __name__ == '__main__':
    generate_words()
