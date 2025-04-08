from cryptography.fernet import Fernet, InvalidToken
import os

# Path to key file
KEY_FILE = 'secret.key'

def generate_key():
    return Fernet.generate_key()

def load_key():
    if not os.path.exists(KEY_FILE):
        key = generate_key()
        with open(KEY_FILE, 'wb') as f:
            f.write(key)
    else:
        with open(KEY_FILE, 'rb') as f:
            key = f.read()
    return key

# Load or create key
key = load_key()
cipher_suite = Fernet(key)

def encrypt(message):
    if message:
        return cipher_suite.encrypt(message.encode('utf-8')).decode('utf-8')  # decode so you can store it in DB
    return None

def decrypt(encrypted):
    try:
        return cipher_suite.decrypt(encrypted.encode('utf-8')).decode('utf-8')
    except InvalidToken:
        print("Invalid token detected!")
        return None
