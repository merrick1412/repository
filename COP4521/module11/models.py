from flask_sqlalchemy import SQLAlchemy
from encrypt import encrypt, decrypt
db = SQLAlchemy()

class Customer(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    security_role_level = db.Column(db.Integer, nullable=False)
    login_password = db.Column(db.String(100), nullable=False)
    def set_name(self, name):
        self.name = encrypt(name)
    def get_name(self):
        return decrypt(self.name)
    def set_phone_number(self, phone_number):
        self.phone_number = encrypt(phone_number)
    def get_phone_number(self):
        return decrypt(self.phone_number)
    def set_login_password(self, password):
        self.login_password = encrypt(password)
    def get_login_password(self):
        return decrypt(self.login_password)

class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    item_sku = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    credit_card_num = db.Column(db.String(16), nullable=False)
    def set_credit_card_num(self, credit_card_num):
        self.credit_card_num = encrypt(credit_card_num)
    def get_credit_card_num(self):
        return decrypt(self.credit_card_num)