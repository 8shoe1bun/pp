from Cryptodome.Cipher import DES
from Cryptodome.Random import get_random_bytes
def pad(text):
    while len(text) % 8 != 0:
        text += b'\x00'
    return text
def des_encrypt(key, plaintext):
    cipher = DES.new(key, DES.MODE_ECB)
    plaintext_bytes  = plaintext.encode('utf-8')
    padded_plaintext = pad(plaintext_bytes)
    ciphertext       = cipher.encrypt(padded_plaintext)
    return ciphertext
def des_decrypt(key, ciphertext):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_plaintext = cipher.decrypt(ciphertext)
    return padded_plaintext.rstrip(b'\x00').decode('utf-8')
key = get_random_bytes(8)
print("Key: ", key.hex())
plaintext = input("Enter the plaintext:")
ciphertext = des_encrypt(key, plaintext)
ciphertext_hex = ciphertext.hex()
decrypted_text = des_decrypt(key, ciphertext)
print("Plaintext: ", plaintext)
print("Ciphertext: ", ciphertext_hex)
print("Decrypted text: ", decrypted_text)
