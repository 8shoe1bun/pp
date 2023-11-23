import numpy as np
keyMatrix = [[0] * 3 for i in range(3)]
messageVector = [[0] for i in range(3)]
cipherMatrix = [[0] for i in range(3)]
inverseKeyMatrix = [[0] * 3 for i in range(3)]


def getKeyMatrix(key):
    k = 0
    for i in range(3):
        for j in range(3):
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1


def calculateDeterminant(matrix):
    return matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) - \
        matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) + \
        matrix[0][2] * (matrix[1][0] * matrix[2][1] -
                        matrix[1][1] * matrix[2][0])


def modInverse(determinant, modulo):
    for i in range(1, modulo):
        if (determinant * i) % modulo == 1:
            return i
    return 1





def calculateAdjugate(matrix):
    adjugate = [[0] * 3 for i in range(3)]
    adjugate[0][0] = matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]
    adjugate[0][1] = matrix[0][2] * matrix[2][1] - matrix[0][1] * matrix[2][2]
    adjugate[0][2] = matrix[0][1] * matrix[1][2] - matrix[0][2] * matrix[1][1]
    adjugate[1][0] = matrix[1][2] * matrix[2][0] - matrix[1][0] * matrix[2][2]
    adjugate[1][1] = matrix[0][0] * matrix[2][2] - matrix[0][2] * matrix[2][0]
    adjugate[1][2] = matrix[0][2] * matrix[1][0] - matrix[0][0] * matrix[1][2]
    adjugate[2][0] = matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]
    adjugate[2][1] = matrix[0][1] * matrix[2][0] - matrix[0][0] * matrix[2][1]
    adjugate[2][2] = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return adjugate


def inverseMatrix(matrix, modulo):
    determinant = calculateDeterminant(matrix)
    mod_inverse = modInverse(determinant, modulo)
    adjugate = calculateAdjugate(matrix)
    inverse = [[(mod_inverse * adjugate[i][j]) %
                modulo for j in range(3)] for i in range(3)]
    return inverse


def decrypt(cipherMatrix, inverseKeyMatrix):
    messageVector = np.dot(inverseKeyMatrix, cipherMatrix) % 26
    plaintext = ""
    for i in range(3):
        plaintext += chr(messageVector[i][0] + 65)
    return plaintext


def HillCipher(message, key):
    getKeyMatrix(key)
    for i in range(3):
        messageVector[i][0] = ord(message[i]) % 65

    for i in range(3):
        cipherMatrix[i][0] = 0
        for x in range(3):
            cipherMatrix[i][0] += (keyMatrix[i][x] * messageVector[x][0])
        cipherMatrix[i][0] = cipherMatrix[i][0] % 26

    CipherText = []
    for i in range(3):
        CipherText.append(chr(cipherMatrix[i][0] + 65))
    print("Ciphertext: ", "".join(CipherText))

    # Calculate the inverse key matrix
    inverseKeyMatrix = inverseMatrix(keyMatrix, 26)

    # Decrypt the cipher text
    decrypted_text = decrypt(cipherMatrix, inverseKeyMatrix)
    print("Decrypted text: ", decrypted_text)

# Driver Code

def main():
    message = input("Enter the plaintext: ").upper()  # "ACT"
    key = input("Enter the key: ").upper()  # "GYBNQKURP"
    HillCipher(message, key)

if __name__=="__main__":
    main()
