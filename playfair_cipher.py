import re

def generate_key_square(key):
    # Remove non-alphabetic characters and convert to uppercase
    key = re.sub(r"[^A-Za-z]", "", key).upper()
    key = key.replace("J", "I")  # Replace J with I
    key_square = list(key)
    for i in range(ord("A"), ord("Z") + 1):
        if chr(i) != "J" and chr(i) not in key_square:
            key_square.append(chr(i))
    return key_square


def generate_bi_pairs(plaintext):
    # Remove non-alphabetic characters and convert to uppercase
    plaintext = re.sub(r"[^A-Za-z]", "", plaintext).upper()
    plaintext = re.sub(r"J", "I", plaintext)  # Replace J with I
    bi_pairs = re.findall(r"(?:(\w)(?!\1)(\w))", plaintext)

    if len(bi_pairs[-1]) == 1:  # If the last bigram has only one letter then add a padding letter
        bi_pairs[-1] = bi_pairs[-1] + ("X",)
    return bi_pairs


def separate_same_letters(plaintext):
    index = 0
    while index < len(plaintext):
        l1 = plaintext[index]
        if index == len(plaintext) - 1:
            plaintext = plaintext + 'X'
            index += 2
            continue
        l2 = plaintext[index + 1]
        if l1 == l2:
            plaintext = plaintext[:index + 1] + "X" + plaintext[index + 1:]
        index += 2
    return plaintext


def find_position(key_square, letter):
    position = key_square.index(letter)
    row = position // 5
    col = position % 5
    return row, col


def encrypt(plaintext, key):
    key_square = generate_key_square(key)
    plaintext = separate_same_letters(plaintext)
    bi_pairs = generate_bi_pairs(plaintext)
    ciphertext = ""
    for pair in bi_pairs:
        char1 = pair[0]
        char2 = pair[1]
        row1, col1 = find_position(key_square, char1)
        row2, col2 = find_position(key_square, char2)
        if row1 == row2:  # If both letters are in the same row
            col1 = (col1 + 1) % 5
            col2 = (col2 + 1) % 5
        elif col1 == col2:  # If both letters are in the same column
            row1 = (row1 + 1) % 5
            row2 = (row2 + 1) % 5
        else:  # If letters are in different rows and columns
            col1, col2 = col2, col1
        ciphertext += key_square[row1 * 5 + col1] + key_square[row2 * 5 + col2]
    return ciphertext


def decrypt(ciphertext, key):
    key_square = generate_key_square(key)
    bi_pairs = generate_bi_pairs(ciphertext)
    plaintext = ""
    for pair in bi_pairs:
        char1 = pair[0]
        char2 = pair[1]
        row1, col1 = find_position(key_square, char1)
        row2, col2 = find_position(key_square, char2)
        if row1 == row2:  # If both letters are in the same row
            col1 = (col1 - 1) % 5
            col2 = (col2 - 1) % 5
        elif col1 == col2:  # If both letters are in the same column
            row1 = (row1 - 1) % 5
            row2 = (row2 - 1) % 5
        else:  # If letters are in different rows and columns
            col1, col2 = col2, col1
        plaintext += key_square[row1 * 5 + col1] + key_square[row2 * 5 + col2]
    return plaintext

plaintext = input("Enter the plaintext: ")
key = input("Enter the key: ")

# Encryption
ciphertext = encrypt(plaintext, key)
print("Cipher_text:", ciphertext)

# Decryption
decrypted_plaintext = decrypt(ciphertext, key)
print("Plain_text:", decrypted_plaintext)
