import os

from cryptography.fernet import Fernet


class Config:
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///customers'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_RECYCLE = 300
    SQLALCHEMY_POOL_TIMEOUT = 1
    encryption_key = b'your_secret_key_here'
    cipher = Fernet(encryption_key)

