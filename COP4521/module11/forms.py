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
