from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    security_role_level = db.Column(db.Integer, nullable=False)
    login_password = db.Column(db.String(100), nullable=False)

    def set_name(self, name):
        self.name = encrypt_data(name)
    def get_name(self):
        return decrypt_data(self.name)
    def set_phone_number(self, phone_number):
        self.phone_number = encrypt_data(phone_number)
    def get_phone_number(self):
        return decrypt_data(self.phone_number)
    def set_login_password(self, password):
        self.login_password = encrypt_data(password)
    def get_login_password(self):
        return decrypt_data(self.login_password)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    item_sku = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    credit_card_num = db.Column(db.String(16), nullable=False)