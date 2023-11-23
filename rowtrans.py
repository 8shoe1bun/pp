# def row_transposition_encrypt(plain_text, key):
#     num_columns = len(key)
#     num_rows = -(-len(plain_text) // num_columns)  # Ceiling division

#     matrix = [['' for _ in range(num_columns)] for _ in range(num_rows)]
#     index = 0
#     for row in range(num_rows):
#         for col in range(num_columns):
#             if index < len(plain_text):
#                 matrix[row][col] = plain_text[index]
#                 index += 1

#     encrypted_text = ''
#     for col in key:
#         encrypted_text += ''.join(matrix[row][col - 1] for row in range(num_rows))

#     return encrypted_text

# def row_transposition_decrypt(encrypted_text, key):
#     num_columns = len(key)
#     num_rows = -(-len(encrypted_text) // num_columns)  # Ceiling division

#     col_lengths = [len(encrypted_text) // num_columns] * num_columns
#     remainder = len(encrypted_text) % num_columns
#     for col in range(remainder):
#         col_lengths[col] += 1

#     matrix = [['' for _ in range(num_columns)] for _ in range(num_rows)]
#     index = 0
#     for col in key:
#         for row in range(col_lengths[col - 1]):
#             matrix[row][col - 1] = encrypted_text[index]
#             index += 1
            
#     decrypted_text = ''
#     for row in range(num_rows):
#         for col in range(num_columns):
#             if matrix[row][col]:
#                 decrypted_text += matrix[row][col]

#     return decrypted_text

# plain_text = "ATTACKPOSTPONEDUNTILTWOAM"
# key = [4,3,1,2,5,6,7]

# encrypted_text = row_transposition_encrypt(plain_text, key)
# print("Encrypted:", encrypted_text)

# decrypted_text = row_transposition_decrypt(encrypted_text, key)
# print("Decrypted:", decrypted_text)

def row_transposition_encrypt(plain_text, key):
    num_columns = len(key)
    num_rows = -(-len(plain_text) // num_columns)  # Ceiling division

    # Fill the matrix with the plain text and special characters
    matrix = [['' for _ in range(num_columns)] for _ in range(num_rows)]
    index = 0
    for row in range(num_rows):
        for col in range(num_columns):
            if index < len(plain_text):
                matrix[row][col] = plain_text[index]
                index += 1

    # Encrypt using the key order
    encrypted_text = ''
    for col in key:
        encrypted_text += ''.join(matrix[row][col - 1] for row in range(num_rows))

    return encrypted_text

def row_transposition_decrypt(encrypted_text, key):
    num_columns = len(key)
    num_rows = -(-len(encrypted_text) // num_columns)  # Ceiling division

    # Determine the lengths of columns based on encrypted text length
    col_lengths = [len(encrypted_text) // num_columns] * num_columns
    remainder = len(encrypted_text) % num_columns
    for col in range(remainder):
        col_lengths[col] += 1

    # Create the matrix with encrypted text
    matrix = [['' for _ in range(num_columns)] for _ in range(num_rows)]
    index = 0
    for col in key:
        for row in range(col_lengths[col - 1]):
            matrix[row][col - 1] = encrypted_text[index]
            index += 1

    # Decrypt the matrix
    decrypted_text = ''
    for row in range(num_rows):
        for col in range(num_columns):
            if matrix[row][col]:
                decrypted_text += matrix[row][col]

    return decrypted_text

plain_text = "HELLO WORLD!"
key = [3, 1, 4, 2]
encrypted_text = row_transposition_encrypt(plain_text, key)
print("Encrypted:", encrypted_text)
decrypted_text = row_transposition_decrypt(encrypted_text, key)
print("Decrypted:", decrypted_text)