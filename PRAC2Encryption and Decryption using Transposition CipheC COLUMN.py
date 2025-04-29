# write a java/c/c++/python program to perform encryption and decryption using the method of Transposition technique

import math

def encrypt_message(message, key):
    cipher = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(message):
            cipher[col] += message[pointer]
            pointer += key
    return ''.join(cipher)
def decrypt_message(cipher_text, key):
    num_of_columns = math.ceil(len(cipher_text) / key)
    num_of_rows = key
    num_of_shaded_boxes = (num_of_columns * num_of_rows) - len(cipher_text)
    plaintext = [''] * num_of_columns
    col = 0
    row = 0
    for symbol in cipher_text:
        plaintext[col] += symbol
        if (col == num_of_columns) or (col == num_of_columns - 1 and row >= num_of_rows - num_of_shaded_boxes):
            col = 0
            row += 1
    return ''.join(plaintext)
message = "AISHWARYA JADAHAV"
key = 6
message = message.replace(" ", "")
print(f"Original Message: {message}")
encrypted = encrypt_message(message, key)
print(f"Encrypted Message: {encrypted}")
decrypted = decrypt_message(encrypted, key)
print(f"Decrypted Message: {decrypted}")
