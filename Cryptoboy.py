import string


def encrypt(file, key, outfile):
    """
    Encrypts the contents of an input file using the Caesar cipher encryption algorithm and writes the ciphertext to an output file.

    Args:
    input_file (str): The name of the input file to encrypt.
    key (int): The key to use for encryption.
    output_file (str): The name of the output file to write the encrypted ciphertext to.
    """

    alphabet = list(string.ascii_uppercase)

    with open(file, 'r') as f_in:
        plaintext = f_in.read()

    uppertext = ""
    ciphertext = ''
    for char in plaintext:
        uppertext += char.upper()

    for char in uppertext:
        if char in alphabet:
            index = alphabet.index(char)
            index = (index + key) % 26
            ciphertext += alphabet[index]
        else:
            ciphertext += char

    with open(outfile, 'w') as f_out:
        f_out.write(ciphertext)


def decrypt(file, key, outfile):
    """
    Decrypts the contents of an input file using the Caesar cipher encryption algorithm and writes the ciphertext to an output file.

    Args:
    input_file (str): The name of the input file to encrypt.
    key (int): The key to use for encryption.
    output_file (str): The name of the output file to write the encrypted ciphertext to.
    """

    alphabet = list(string.ascii_uppercase)

    with open(file, 'r') as f_in:
        plaintext = f_in.read()

    uppertext = ""
    ciphertext = ''
    for char in plaintext:
        uppertext += char.upper()

    for char in uppertext:
        if char in alphabet:
            index = alphabet.index(char)
            index = (index - key) % 26
            ciphertext += alphabet[index]
        else:
            ciphertext += char

    with open(outfile, 'w') as f_out:
        f_out.write(ciphertext)


def crack(file, threshold):
    pass


def check():
    pass
