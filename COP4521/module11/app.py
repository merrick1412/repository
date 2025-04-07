"""
Name:Merrick Moncure
Date: 4/6/25
Assignmnent: Module 12: website in flask
encrypt necessary data
Assumptions: NA
All work below was performed by Merrick Moncure
"""
from flask import Flask, render_template, redirect, url_for, request, flash, session
from models import db, Customer, Order
from forms import CustomerForm, OrderForm
from config import Config
from encrypt import encrypt,decrypt
import sqlite3



app = Flask(__name__)
app.config.from_object(Config)
print("running app")
db.init_app(app)
#deal with locks


#logging queries
#def log_sql_callback(statement):
#    print("Executing SQL statement:", statement)
#conn.set_trace_callback(log_sql_callback)

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
                credit_card_num=form.credit_card.data.strip()
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

        encrypted_user = encrypt(username) #stores encrypted data now
        encrypted_password = encrypt(password)

        user = Customer.query.filter_by(name=encrypted_user).first()

        if user and user.login_password == encrypted_password:
            session['username'] = user.get_name
            session['security_level'] = user.security_role_level
            flash("Login successful!")
            return redirect(url_for('home'))
        else:
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
        order.credit_card_num = order.get_credit_card_num() #decrypt

    # Return the list_orders.html template with the orders data
    return render_template('list_orders.html', orders=orders)
@app.route('/result')
def result():
    msg = request.args.get('msg', 'No message provided')
    return render_template('result.html', msg=msg)
#makes a table
if __name__ == '__main__':
    with app.app_context():
        print("running here creatall")
        try:
            db.create_all()  # Create tables if they don't exist
        except Exception as e:
            print(f"Error during database initialization: {str(e)}")
    app.run(debug=True)
