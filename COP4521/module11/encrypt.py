#key
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

def generate_key():
    return Fernet.generate_key()

def encrypt(message):
    if message:
        return cipher_suite.encrypt(message.encode('utf-8'))
    return None
def decrypt(encrypted):
    if encrypted:
        return cipher_suite.decrypt(encrypted).decode('utf-8')
    return None