import os

class Config:
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db?timeout=10'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_RECYCLE = 300
    SQLALCHEMY_POOL_TIMEOUT = 1

