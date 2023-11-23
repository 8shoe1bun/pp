def encryption(plain_text, key):
    cipher_text = ""

    enc_matrix = [[" " for i in range(len(plain_text))] for j in range(key)]

    flag = 0
    row = 0

    for i in range(len(plain_text)):
        enc_matrix[row][i] = plain_text[i]

        if row == 0:
            flag = 0
        elif row == key-1:
            flag = 1

        if flag == 0:
            row += 1
        else:
            row -= 1

    # for i in range(key):
    #     print(''.join(enc_matrix[i]))

    for i in range(key):
        for j in range(len(plain_text)):
            if enc_matrix[i][j] != ' ':
                cipher_text += enc_matrix[i][j]

    return cipher_text


def decryption(cipher_text, key):
    dec_matrix = [['\n' for i in range(len(cipher_text))] for j in range(key)]

    dir_down = None
    row, col = 0, 0

    for i in range(len(cipher_text)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        dec_matrix[row][col] = '*'
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    index = 0
    for i in range(key):
        for j in range(len(cipher_text)):
            if ((dec_matrix[i][j] == '*') and (index < len(cipher_text))):
                dec_matrix[i][j] = cipher_text[index]
                index += 1

    result = []
    row, col = 0, 0

    for i in range(len(cipher_text)):
        if row == 0:
            dir_down = True
        if row == key-1:
            dir_down = False

        if (dec_matrix[row][col] != '*'):
            result.append(dec_matrix[row][col])
            col += 1

        if dir_down:
            row += 1
        else:
            row -= 1
            
    return "".join(result)


pt = input("Enter the plaintext: ")
k = int(input("Enter the key: "))

cipher_text = encryption(pt, k)
plain_text = decryption(cipher_text, k)

print("Cipher Text:", cipher_text)
print("Plain Text:", plain_text)


