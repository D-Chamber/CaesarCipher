import string
import os
import re

"""
Dictionary is created to contain words from the dictionary file, so accessing them is a smaller time complexity 
than scrolling through all of them. alphabet is also created in a list 
using lower case and is used by shifting the given
text character by character by the position of the key and the current index.

dictionary (list): stores each word in the dictionary file as an entry.
alphabet (list): stores each letter (ascii_lowercase) as an entry.
"""
dictionary = []
with open('dictionary.txt', 'r') as dictionary_input:
    lines = dictionary_input.readlines()
    for x in lines:
        dictionary.append(x.replace("\n", ""))
    dictionary_input.close()
alphabet = list(string.ascii_lowercase)


def encrypt(file, key, outfile):
    """
    Encrypts the contents of an input file using the Caesar cipher encryption algorithm and writes the ciphertext to
    an output file.

    Args:
    input_file (str): The name of the input file to encrypt.
    key (int): The key to use for encryption.
    output_file (str): The name of the output file to write the encrypted ciphertext to.
    """

    # checks to see if file exists within the current directory if it does it continue with the encryption,
    # if not it prints out the error message
    if not os.path.exists(file):
        print(f'{file} does not exist in current directory')

    else:
        with open(file, 'r') as f_in:
            plaintext = f_in.read()

        lowertext: str = ""
        ciphertext: str = ''
        for char in plaintext:
            lowertext += char.lower()

        for char in lowertext:
            if char in alphabet:
                index = alphabet.index(char)
                index = (index + key) % 26
                ciphertext += alphabet[index]
            else:
                ciphertext += char

        with open(outfile, 'w') as f_out:
            f_out.write(ciphertext)

        print(f"{file} encryption was successful with key {key}, stored in {outfile}.")

        f_in.close()
        f_out.close()


def decrypt(file, key, outfile):
    """
    Decrypts the contents of an input file using the Decryption algorithm and outputs to the specified file name.

    Args:
    input_file (str): The name of the input file to encrypt.
    key (int): The key to use for encryption.
    output_file (str): The name of the output file to write the encrypted ciphertext to.
    """

    # checks to see if file exists within the current directory if it does it continue with the encryption,
    # if not it prints out the error message

    if not os.path.exists(file):
        print(f'{file} does not exist in current directory')

    else:
        # this decryption part runs if all 3 arguments are passed
        if file is not None and key is not None and outfile is not None:
            with open(file, 'r') as f_in:
                ciphertext = f_in.read()

            lowertext = ""
            plaintext = ''
            for char in ciphertext:
                lowertext += char.lower()

            for char in lowertext:
                if char in alphabet:
                    index = alphabet.index(char)
                    index = (index - key) % 26
                    plaintext += alphabet[index]
                else:
                    plaintext += char

            with open(outfile, 'w') as f_out:
                f_out.write(plaintext)

            print(f"{file} decryption was successful with key {key}, stored in {outfile}.")

            f_in.close()
            f_out.close()

        # this part will run if only 2 arguments are passed (the file name and the key, outfile is not required)
        elif file is not None and key is not None and outfile is None:
            with open(file, 'r') as f_in:
                ciphertext = f_in.read()

            lowertext = ''
            plaintext = ''

            for char in ciphertext:
                lowertext += char.lower()

            for char in lowertext:
                if char in alphabet:
                    index = alphabet.index(char)
                    index = (index - key) % 26
                    plaintext += alphabet[index]
                else: # replaces everything that is not a letter with spaces since this file is not being written to a file.
                    plaintext += " "

            return plaintext


def crack(file, threshold):
    """
    :param file: takes a string of the file that we are going to brute-force/decrypt
    :param threshold: is the percent that the cracking needs to determine if it was successful.
    :return: None
    """

    # Checks if the file exists within the current directory
    if not os.path.exists(file):
        print(f'{file} does not exist in current directory')

    else:
        # initiates the value of best key and match_percentage
        bestkey: int = 0
        match_percentage: float = 0

        # this iterates through each key till the end of the length of the alphabet.
        for key in range(len(alphabet) + 1):
            # runs the decrypt function each time and delimits the word_list by either the " symbol or an empty space.
            temp_decrypt = decrypt(file, key, None)
            word_list = re.split(" |\"", temp_decrypt)

            # goes through the list again and removes empty string from the list.
            for i in word_list:
                if len(i) == 0:
                    word_list.remove(i)

            # runs the check function that returns a percentage that is used to determine which key is best.
            temp_percentage = check(word_list)
            if temp_percentage > match_percentage:
                match_percentage = temp_percentage
                bestkey = key

        if match_percentage > threshold:
            print(f'Crack was successful using the key {bestkey}, with a {round(match_percentage*100, 2)}% using '
                  f'a threshold of {round(threshold*100, 2)}%')

        else:
            print(f'Crack was unsuccessful at {round(threshold*100), 2}% threshold.')


def check(text):
    """
    :param text: just takes the list of words
    :return: the percentage of matching words in the dictionary as a float
    """
    text_list = text

    matches = 0
    for text in text_list:
        if text in dictionary:
            matches += 1

    return matches/ len(text_list)
