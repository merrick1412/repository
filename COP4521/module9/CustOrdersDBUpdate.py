"""
Name:Merrick Moncure
Date: 3/15/25
Assignmnent: Module 9: SQLite3 Database
create an sql database
Assumptions: NA
All work below was performed by Merrick Moncure
"""
import sqlite3
conn = sqlite3.connect('customer_orders.db')
cursor = conn.cursor()

#delete data
cursor.execute("DELETE FROM Customer WHERE CustId = 4")

#update data
cursor.execute("UPDATE Customer SET Age = 33 WHERE Name = 'AMath'")
cursor.execute("UPDATE Order SET Price = 100 WHERE OrderId = 2")

#select data
cursor.execute("SELECT * FROM Customer")
print("All customers:")
for row in cursor.fetchall():
    print(row)
cursor.execute("SELECT Name, Age FROM Customer")
print("\nCustomer name and age:")
for row in cursor.fetchall():
    print(row)
cursor.execute("SELECT * FROM Customer WHERE Age > 30")
print("\nCustomers older than 30:")
for row in cursor.fetchall():
    print(row)
cursor.execute("SELECT Name, Age FROM Customer WHERE Age > 30")
print("\nCustomers older than 30 with selected columns:")
for row in cursor.fetchall():
    print(row)
conn.commit()
conn.close()