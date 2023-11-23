# Encryption

def caesar_encryption(plaintext, key):
    ciphertext = ""
    # check if there is a space and  it is replaced
    plaintext = plaintext.replace(" ", "")
    for char in plaintext:
        # check the char is alphabet
        if char.isalpha():
            # if char is uppercase ascii value will be 65 else lowercase means 97
            ascii_code = ord('A') if char.isupper() else ord('a')
            # formula to covert plaintext to cipertext
            shifted_char = chr(
                (ord(char) - ascii_code + key) % 26 + ascii_code)  # This subtraction normalizes the range of characters from 0 to 25 and adds the key and take modulusnext add back the ascii value
            ciphertext += shifted_char
        else:
            ciphertext += char
    return ciphertext

# decryption


def caesar_decryption(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        # check the char is alphabet
        if char.isalpha():
            # if char is uppercase ascii value will be 65 else lowercase means 97
            ascii_code = ord('A') if char.isupper() else ord('a')
            # formula to covert ciphertext to plaintext
            shifted_char = chr(
                (ord(char) - ascii_code - key) % 26 + ascii_code)
            plaintext += shifted_char
        else:
            plaintext += char
    return plaintext


plaintext = input("Enter the plaintext:")
key = int(input("Enter the key:"))

ciphertext = caesar_encryption(plaintext, key)
decrypted_plaintext = caesar_decryption(ciphertext, key)

print("Cipher_text:", ciphertext)
print("Plain_text:", decrypted_plaintext)
