from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding


def generate_rsa_keypair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    return private_key, public_key


def create_digital_signature(message, private_key):
    signature = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature


def verify_digital_signature(message, signature, public_key):
    try:
        public_key.verify(
            signature,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return "Valid"
    except :
        return "Not valid"


input_message = input("Enter a message: ").encode("utf-8")

private_key, public_key = generate_rsa_keypair()
signature = create_digital_signature(input_message, private_key)

print("Signature Value:\n",signature.hex())
print("Length of Signature:",len(signature.hex()))
modify_message = input("Enter the modified message: ").encode('utf-8')
# print("Verification:", verify_digital_signature(input_message, signature, public_key))
print("Verification:", verify_digital_signature(modify_message, signature, public_key))
