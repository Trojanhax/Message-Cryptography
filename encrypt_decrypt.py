

from cryptography.fernet import Fernet

def generate_key():
    # Function to generate a Fernet key
    return Fernet.generate_key()

def encrypt_message(key, message):
    # Function to encrypt a message with a given key
    cipher = Fernet(key)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message

def decrypt_message(key, encrypted_message):
    # Function to decrypt an encrypted message with a given key
    cipher = Fernet(key)
    decrypted_message = cipher.decrypt(encrypted_message).decode()
    return decrypted_message
