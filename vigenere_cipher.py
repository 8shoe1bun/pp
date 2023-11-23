def vigenere_encrypt(plaintext, key):
    plaintext = plaintext.upper()
    # check if there is a space and  it is replaced
    plaintext = plaintext.replace(" ", "")
    key = key.upper()
    # check if there is a space and  it is replaced
    key = key.replace(" ", "")
    ciphertext = ""
    for i in range(len(plaintext)):
        # formula to covert plaintext to ciphertext
        # The modulus operator % is used to ensure that if the plaintext is longer than the key, the key is repeated cyclically.
        char = chr(
            (ord(plaintext[i]) + ord(key[i % len(key)]) - 2 * 65) % 26 + 65)
        # Subtracting this value (2 times the Unicode value of 'A') is used to normalize the range of the values so that 'A' has a value of 0.
        ciphertext += char
    return ciphertext


def vigenere_decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = key.upper()
    plaintext = ""
    for i in range(len(ciphertext)):
        # formula to convert ciphertext to plaintext
        char = chr(
            (ord(ciphertext[i]) - ord(key[i % len(key)]) + 26) % 26 + 65)
        plaintext += char
    return plaintext


plaintext = input("Enter the plaintext: ")
key = input("Enter the key:   ")

ciphertext = vigenere_encrypt(plaintext, key)
decrypted_plaintext = vigenere_decrypt(ciphertext, key)

print("Cipher_text:", ciphertext)
print("Plain_text:", decrypted_plaintext)
