"""
Name:Merrick Moncure
Date: 3/15/25
Assignmnent: Module 9: SQLite3 Database
create an sql database
Assumptions: NA
All work below was performed by Merrick Moncure
"""
import sqlite3

conn = sqlite3.connect('customer.db')
cursor = conn.cursor()

#drop the table
cursor.execute("DROP TABLE IF EXISTS Customer")

#make the table
cursor.execute("""
CREATE TABLE Customer (
    CustId INTEGER PRIMARY KEY,
    Name TEXT,
    Age INTEGER,
    PhNum TEXT,
    SecurityLevel INTEGER,
    LoginPassword TEXT
)
""")
#insert data

cursor.executemany("""
INSERT INTO Customer (CustId, Name, Age, PhNum, SecurityLevel, LoginPassword)
VALUES (?, ?, ?, ?, ?, ?)
""", [
    (1, 'PDiana', 34, '123-675-7645', 1, 'test123'),
    (2, 'TJones', 68, '895-345-6523', 2, 'test123'),
    (3, 'AMath', 29, '428-197-3967', 3, 'test123'),
    (4, 'BSmith', 37, '239-567-3498', 2, 'test123')
])
#display
cursor.execute("SELECT * FROM Customer")
for row in cursor:
    print(row)
conn.commit()
conn.close()
print("connection closed.")