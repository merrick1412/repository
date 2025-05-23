"""
Name:Merrick Moncure
Date: 4/13/25
Assignmnent: Module 13: website in flask
use a socket server to send orders to the process_orders_server.py
Assumptions: NA
All work below was performed by Merrick Moncure
"""
from cryptography import fernet
from flask import Flask, render_template, redirect, url_for, request, flash, session
from sqlalchemy import text

from models import db, Customer, Order
from forms import CustomerForm, OrderForm
from config import Config
from encrypt import encrypt,decrypt
import sqlite3
import socket



app = Flask(__name__)
app.config.from_object(Config)
print("running app")
db.init_app(app)



#using dml to fill initial table
def test_data():
    with app.app_context():
        # Create customers and use setter methods for encrypted fields
        customers = []

        # List of raw customer info (unencrypted)
        customer_data = [
            ("John Doe", 30, "1234567890", 1, "password123"),
            ("Jane Smith", 28, "0987654321", 2, "securePass1"),
            ("Alice Johnson", 35, "5555555555", 1, "alicePass3"),
            ("Bob Brown", 40, "6666666666", 2, "bobSecure123"),
            ("Charlie Green", 50, "7777777777", 3, "charliePass2"),
            ("Dana White", 22, "8888888888", 1, "dana123")
        ]

        for name, age, phone, role, password in customer_data:
            customer = Customer(
                age=age,
                security_role_level=role
            )
            customer.set_name(name)
            customer.set_phone_number(phone)
            customer.set_login_password(password)

            customers.append(customer)
            db.session.add(customer)

        db.session.commit()

        # Now that customer IDs are assigned, add orders
        order_data = [
            (1, "ABC123", 1, 100, "4111111111111111"),
            (2, "DEF456", 2, 50, "4222222222222222"),
            (3, "GHI789", 1, 200, "4333333333333333"),
            (4, "JKL101", 3, 30, "4444444444444444"),
            (5, "MNO202", 2, 120, "4555555555555555"),
            (6, "PQR303", 4, 80, "4666666666666666")
        ]

        for cust_id, sku, quantity, price, cc_num in order_data:
            order = Order(
                customer_id=cust_id,
                item_sku=sku,
                quantity=quantity,
                price=price
            )
            order.set_credit_card_num(cc_num)
            db.session.add(order)

        db.session.commit()

@app.before_request
def before_request():
    db.session.remove()
@app.after_request
def after_request(response):
    db.session.remove()
    return response
#adding orders
@app.route('/add_order', methods=['GET','POST'])
def add_order():
    if 'username' not in session:
        flash("You need to log in first")
        return redirect(url_for('login'))
    form = OrderForm()
    if form.validate_on_submit():
        try:
            #validate the data
            item_sku = form.item_sku.data.strip()
            if not item_sku:
                flash("Item SKU cannot be empty or only spaces", "error")
                return redirect(url_for('add_order'))

            # Quantity must be greater than 0
            quantity = form.quantity.data
            if quantity <= 0:
                flash("Quantity must be greater than 0", "error")
                return redirect(url_for('add_order'))

            # Price must be greater than 0
            price = form.price.data
            if price <= 0:
                flash("Price must be greater than 0", "error")
                return redirect(url_for('add_order'))

            # Credit Card number cannot be empty or only spaces
            credit_card = form.credit_card.data.strip()
            if not credit_card:
                flash("Credit Card number cannot be empty or only spaces", "error")
                return redirect(url_for('add_order'))
            encrypt_credit_card = encrypt(credit_card)
            order = Order(
                customer_id=session['username'],
                item_sku=form.item_sku.data.strip(),
                quantity=form.quantity.data,
                price=form.price.data,
                credit_card_num=encrypt_credit_card
            )
            #uses encrypted method in models
            order.set_credit_card_num(form.credit_card.data)

            db.session.add(order)
            db.session.commit()
            flash("Order added successfully")
            return redirect(url_for('home'))
        except Exception as e:
            db.session.rollback() #in case of error
            flash(f"An error occurred while adding the order: {str(e)}", "error")
            return redirect(url_for('add_order'))

    return render_template('add_order.html', form=form)
#sends to home
@app.route('/')
def home():
    if 'username' in session:
        username = session['username']
        security_level = session['security_level']
        return render_template('home.html', username=username,security_level=security_level)
    else:
        flash("You need to log in first") #redirects to login page
        return redirect(url_for('login'))
@app.route('/logout')
def logout():
    session.clear()
    flash("Logged out successfully.")
    return redirect(url_for('login'))
#login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'] #checks db for login
        password = request.form['password']

        all_users = Customer.query.all()

        user = None

        for u in all_users:
            if u.get_name() == username:
                user = u
                break

        if user:
            decrypted_password = user.get_login_password()
            if decrypted_password == password:
                session['username'] = user.get_name()
                session['security_level'] = user.security_role_level
                flash("Login successful!")
                return redirect(url_for('home'))
        flash("Invalid login!")
        return render_template('login.html')

    return render_template('login.html')

#add customer page
@app.route('/add_customer', methods=['GET', 'POST'])
def add_customer():
    if 'username' not in session or session.get('security_level') < 2:
        flash("Missing security level")
        return redirect(url_for('home'))
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
        #encrypt data
        encrypted_name, encrypted_phone_number, encrypted_login_password = encrypt(form.name.data.strip()), encrypt(form.phone_number.data.strip()), encrypt(form.login_password.data.strip())
        #creating the new customer

        new_customer = Customer(
            name=encrypted_name,
            age=form.age.data,
            phone_number=encrypted_phone_number,
            security_role_level=form.security_role_level.data,
            login_password=encrypted_login_password
        )

        db.session.add(new_customer)
        db.session.commit()
        flash("Customer added successfully!", "success")
        return redirect(url_for('result', msg="Customer added successfully!"))
    return render_template('add_customer.html', form=form)

@app.route('/list_customers')
def list_customers():
    customers = Customer.query.all()
    for customer in customers:
        customer.name = customer.get_name() #decrypt all the data
        customer.phone_number = customer.get_phone_number()
        customer.login_password = customer.get_login_password()
    return render_template('list_customers.html', customers=customers)

@app.route('/show_orders')
def show_orders():
    if 'username' not in session:
        flash("You must log in first")
        return redirect(url_for('login')) #make sure you see your orders
    user_orders = Order.query.filter_by(customer_id=session['username']).all()
    for order in user_orders:
        try:
            order.credit_card_num = order.get_credit_card_num()
        except Exception as e:
            order.credit_card_num = '[Decryption Failed]'
    return render_template('show_orders.html',orders=user_orders)
@app.route('/list_orders')
def list_orders():
    #check if the user is logged in and has the correct security level
    if 'username' not in session or session.get('security_level') < 2:
        flash("You do not have permission to view this page.")
        return redirect(url_for('login'))

    # Fetch all orders from the database
    orders = Order.query.all()
    for order in orders:
        customer = Customer.query.get(order.customer_id)
        if customer:
            try:
                customer_name = customer.get_name()
            except Exception as e:
                print(f"Failed to decrypt name for customer_id {order.customer_id}: {e}")
                customer_name = "Unknown"
        else:
            customer_name = "Unknown"
        order.customer_name = customer_name

        order.product = order.item_sku
        order.status = "Processed"

    return render_template('list_orders.html', orders=orders)
@app.route('/result')
def result():
    msg = request.args.get('msg', 'No message provided')
    return render_template('result.html', msg=msg)
#makes a table

@app.route('/submit_order_socket', methods=['GET', 'POST'])
def submit_order_socket():
    if 'username' not in session:
        return redirect(url_for('login'))

    form = OrderForm()

    if request.method == 'POST' and form.validate_on_submit():
        username = session['username']

        #  Find the actual numeric customer ID from the name
        all_customers = Customer.query.all()
        cust_id = None
        for c in all_customers:
            if c.get_name() == username:
                cust_id = c.id
                break

        if not cust_id:
            flash("Customer not found in the database.")
            return render_template("add_order.html", form=form)

        # Get cleaned form data
        item_sku = form.item_sku.data.strip()
        quantity = form.quantity.data
        price = form.price.data
        credit_card = form.credit_card.data.strip()

        # Basic validation (extra)
        if not item_sku or not credit_card or quantity <= 0 or price <= 0:
            flash("Validation failed: Invalid field values.")
            return render_template("add_order.html", form=form)

        try:
            #  Use numeric customer ID in the message
            message = f"{cust_id}^%${item_sku}^%${quantity}^%${price}^%${credit_card}"
            encrypted_message = encrypt(message)

            #  Send to socket server
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect(('localhost', 9999))
                s.sendall(encrypted_message.encode('utf-8'))

            return redirect(url_for("result", msg="Order successfully sent"))

        except Exception as e:
            print("Socket Error:", e)
            return redirect(url_for("result", msg="Error - Order NOT sent"))

    # Show form on GET or failed POST
    return render_template("add_order.html", form=form)


if __name__ == '__main__':
    with app.app_context():
        db.session.execute(text("DROP TABLE IF EXISTS Customer")) #drop tables
        db.session.execute(text('DROP TABLE IF EXISTS "Order"'))
        db.create_all()  # Create tables

    test_data()
    app.run(debug=True)
