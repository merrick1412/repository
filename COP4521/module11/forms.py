from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Length

class CustomerForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=100)])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=1, max=120)])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    security_role_level = IntegerField('Security Role Level', validators=[DataRequired(), NumberRange(min=1, max=3)])
    login_password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Add Customer')

class OrderForm(FlaskForm):
    item_sku = StringField('Item SKU', validators=[DataRequired(message="Item SKU is required")])
    quantity = IntegerField('Quantity', validators=[DataRequired(message="Quantity is required"), NumberRange(min=1, message="Quantity must be greater than 0")])
    price = FloatField('Price', validators=[DataRequired(message="Price is required"), NumberRange(min=0.01, message="Price must be greater than 0")])
    credit_card = StringField('Credit Card Number', validators=[DataRequired(message="Credit Card number is required")])
    submit = SubmitField('Add Order')
