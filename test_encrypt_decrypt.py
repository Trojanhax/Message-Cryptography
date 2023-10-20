

from encrypt_decrypt import generate_key, encrypt_message, decrypt_message

def test_encrypt_decrypt():
    key = generate_key()
    message = input(" eter your massage:--- ")

    encrypted_message = encrypt_message(key, message)
    decrypted_message = decrypt_message(key, encrypted_message)
    if message == decrypted_message:
        print("Original Message:", message)
        print("Decrypted Message:", decrypted_message)
        print("Key:", key)
    else:
        print("Decryption failed!")

test_encrypt_decrypt()


