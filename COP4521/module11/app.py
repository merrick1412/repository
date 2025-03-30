"""
Name:Merrick Moncure
Date: 3/23/25
Assignmnent: Module 10: website in flask
make a simple flask website
Assumptions: NA
All work below was performed by Merrick Moncure
"""
from flask import Flask, render_template, redirect, url_for, request, flash
from models import db, Customer, Order
from forms import CustomerForm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
us
#sends to home
@app.route('/')
def home():
    return render_template('home.html')
#login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users_db and users_db[username]['password'] == password:
            session['username'] = username
            session['security_level'] = users_db[username]['security_level']
            flash("Login successful!")
            return redirect(url_for('home'))
        else:
            flash("Invalid login!")
            return render_template('login.html')

    return render_template('login.html')

#add customer page
@app.route('/add_customer', methods=['GET', 'POST'])
def add_customer():
    form = CustomerForm()
    #input validation
    if form.validate_on_submit():
        if not form.name.data.strip():
            flash("Name cannot be empty or only spaces", "error")
            return redirect(url_for('add_customer'))
        if not (1 <= form.age.data <= 120):
            flash("Age must be between 1 and 120", "error")
            return redirect(url_for('add_customer'))
        if not form.phone_number.data.strip():
            flash("Phone number cannot be empty or only spaces", "error")
            return redirect(url_for('add_customer'))
        if not (1 <= form.security_role_level.data <= 3):
            flash("Security role level must be between 1 and 3", "error")
            return redirect(url_for('add_customer'))
        if not form.login_password.data.strip():
            flash("Login password cannot be empty or only spaces", "error")
            return redirect(url_for('add_customer'))
        #creating the new customer
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
#makes a table
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
    app.run(debug=True)
