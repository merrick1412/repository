from flask import Flask, render_template, redirect, url_for, request, flash
from models import db, Customer, Order
from forms import CustomerForm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add_customer', methods=['GET', 'POST'])
def add_customer():
    form = CustomerForm()
    if form.validate_on_submit():
        new_customer = Customer(
            name=form.name.data.strip(),
            age=form.age.data,
            phone_number=form.phone_number.data.strip(),
            security_role_level=form.security_role_level.data,
            login_password=form.login_password.data.strip()
        )
        db.session.add(new_customer)
        db.session.commit()
        flash("Customer added successfully!", "success")
        return redirect(url_for('result', msg="Customer added successfully!"))
    return render_template('add_customer.html', form=form)

@app.route('/list_customers')
def list_customers():
    customers = Customer.query.all()
    return render_template('list_customers.html', customers=customers)

@app.route('/list_orders')
def list_orders():
    orders = Order.query.all()
    return render_template('list_orders.html', orders=orders)

@app.route('/result')
def result():
    msg = request.args.get('msg', 'No message provided')
    return render_template('result.html', msg=msg)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
    app.run(debug=True)
