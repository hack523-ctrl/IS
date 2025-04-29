# write a java/c/c++/python program to implement RSA algorithm.

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
def generate_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    return private_key, public_key
def encrypt_message(message, public_key):
    encrypted = public_key.encrypt(
        message.encode('utf-8'),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted
def decrypt_message(encrypted_message, private_key):
    decrypted = private_key.decrypt(
        encrypted_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted.decode('utf-8')
def main():
    message = "TEJAS1608"
    print(f"Original Message: {message}")
    private_key, public_key = generate_keys()
    encrypted_msg = encrypt_message(message, public_key)
    print(f"Encrypted (bytes): {encrypted_msg}")
    print(f"Encrypted (hex): {encrypted_msg.hex()}")
    decrypted_msg = decrypt_message(encrypted_msg, private_key)
    print(f"Decrypted Message: {decrypted_msg}")
if __name__ == "__main__":
    main()
