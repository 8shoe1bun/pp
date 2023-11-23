def row_transposition_encrypt(plain_text, key):
    num_rows = (len(plain_text) + len(key) - 1) // len(key)
    matrix = [['' for _ in range(len(key))] for _ in range(num_rows)]

    index = 0
    for row in matrix:
        for col in range(len(row)):
            if index < len(plain_text):
                row[col] = plain_text[index]
                index += 1

    encrypted_text = ''
    for col in key:
        encrypted_text += ''.join(matrix[row][col - 1]
                                  for row in range(num_rows))

    return encrypted_text


def row_transposition_decrypt(encrypted_text, key):
    num_rows = (len(encrypted_text) + len(key) - 1) // len(key)
    matrix = [['' for _ in range(len(key))] for _ in range(num_rows)]

    col_lengths = [len(encrypted_text) // len(key)] * len(key)
    remainder = len(encrypted_text) % len(key)
    for col in range(remainder):
        col_lengths[col] += 1

    index = 0
    for col in key:
        for row in range(col_lengths[col - 1]):
            matrix[row][col - 1] = encrypted_text[index]
            index += 1

    decrypted_text = ''
    for row in matrix:
        for col in range(len(row)):
            if row[col]:
                decrypted_text += row[col]

    return decrypted_text


# Example usage
plain_text = input("Enter the plaintext: ")
key = []
print("Enter the key order: ")

while True:
    keyOrder = int(input(""))
    if keyOrder == -1 or keyOrder == 0:
        break
    else:
        key.append(keyOrder)

plain_text = plain_text.replace(" ", "")

encrypted_text = row_transposition_encrypt(plain_text, key)
print("Encrypted:", encrypted_text)

decrypted_text = row_transposition_decrypt(encrypted_text, key)
print("Decrypted:", decrypted_text)
