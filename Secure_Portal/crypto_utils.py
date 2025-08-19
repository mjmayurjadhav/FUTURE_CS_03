# crypto_utils.py
from cryptography.fernet import Fernet

def generate_key():
    """
    Generate a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
    Load the previously generated key
    """
    return open("key.key", "rb").read()

def encrypt_data(data, key):
    """
    Encrypt data using the provided key
    """
    f = Fernet(key)
    encrypted = f.encrypt(data)
    return encrypted

def decrypt_data(encrypted_data, key):
    """
    Decrypt data using the provided key
    """
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_data)
    return decrypted

