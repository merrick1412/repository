"""
Name:Merrick Moncure
Date: 3/15/25
Assignmnent: Module 9: SQLite3 Database
create an sql database
Assumptions: NA
All work below was performed by Merrick Moncure
"""
import sqlite3


customer_conn = sqlite3.connect('customer.db')
customer_cursor = customer_conn.cursor()

orders_conn = sqlite3.connect('orders.db')
orders_cursor = orders_conn.cursor()

#deletes 1 row from the Customer table
customer_cursor.execute("DELETE FROM Customer WHERE CustId = 4")


#Update the 'Customer' table (change Age for customer 'AMath')
customer_cursor.execute("UPDATE Customer SET Age = 33 WHERE Name = 'AMath'")

#update the order table (change Price for OrderId 2)
orders_cursor.execute('UPDATE "Order" SET Price = 100 WHERE OrderId = 2')

#select statement from the customer table (select all data)
customer_cursor.execute("SELECT * FROM Customer")
print("All customers:")
for row in customer_cursor.fetchall():
    print(row)

#select statement from the 'Customer' table that limits the columns (Name, Age)
customer_cursor.execute("SELECT Name, Age FROM Customer")
print("\nCustomer name and age:")
for row in customer_cursor.fetchall():
    print(row)

#select statement from the 'Customer' table that limits the rows (Age > 30)
customer_cursor.execute("SELECT * FROM Customer WHERE Age > 30")
print("\nCustomers older than 30:")
for row in customer_cursor.fetchall():
    print(row)

#select statement from the 'Customer' table that limits both columns and rows (Age > 30)
customer_cursor.execute("SELECT Name, Age FROM Customer WHERE Age > 30")
print("\nCustomers older than 30 with selected columns:")
for row in customer_cursor.fetchall():
    print(row)


customer_conn.commit()
orders_conn.commit()


customer_conn.close()
orders_conn.close()