from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes


def pad(text):
    block_size = AES.block_size
    padding_size = block_size - len(text) % block_size
    padded_text = text + \
        padding_size.to_bytes(1, byteorder='big') * padding_size
    return padded_text


def aes_encrypt(key, plaintext):
    cipher = AES.new(key, AES.MODE_CBC)
    padded_plaintext = pad(plaintext.encode('utf-8'))
    ciphertext = cipher.encrypt(padded_plaintext)
    return cipher.iv + ciphertext


def aes_decrypt(key, ciphertext):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    padded_plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    return padded_plaintext.rstrip(b'\x00').decode('utf-8')


key = get_random_bytes(16)
print("Key: ", key.hex())
plaintext = input("Enter the plaintext:")

ciphertext = aes_encrypt(key, plaintext)
decrypted_text = aes_decrypt(key, ciphertext)

print("Plaintext: ", plaintext)
print("Ciphertext: ", ciphertext.hex())
print("Decrypted text: ", decrypted_text.strip())
