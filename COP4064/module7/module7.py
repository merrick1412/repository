"""
name: Merrick Moncure
date: 10/19/2025
assignment: document db search, indexing, and advanced app
course: cop4064

about this file:
- connects to local mongodb using pymongo
- part 1: shows all required finds and updates
- part 2: explain plan before and after adding index
- part 3: menu driven app for gadgets with add, display, update, delete, quit
"""

from pymongo import MongoClient, ASCENDING
from pymongo.errors import DuplicateKeyError
from pprint import pprint

# connect to mongodb
client = MongoClient("mongodb://localhost:27017")
db = client["cop4064_docdb"]
col = db["items"]
gadgets = db["gadgets"]

# make sure there’s some data to work with
def reset_seed():
    col.drop()
    gadgets.drop()
    docs = [
        {"_id": 1, "name": "alpha", "qty": 5, "price": 9.99, "tags": ["blue", "small"], "item": None},
        {"_id": 2, "name": "beta", "qty": 12, "price": 19.5, "tags": ["green"], "item": "exists"},
        {"_id": 3, "name": "gamma", "qty": 50, "price": 29.0, "tags": ["red"], "item": None},
    ]
    col.insert_many(docs)
    gadgets.insert_many([
        {"sku": "g100", "title": "widget one", "specs": {"weight": 1.2, "life": 12, "power": 50.0}},
        {"sku": "g200", "title": "widget two", "specs": {"weight": 0.8, "life": 6, "power": 30.0}}
    ])

reset_seed()

def banner(txt):
    print("\n" + "-" * 60)
    print(txt)
    print("-" * 60)

# part 1 – document db search
banner("1) all items")
for d in col.find({}):
    pprint(d)

banner("2) find using $lt")
for d in col.find({"qty": {"$lt": 10}}):
    pprint(d)

banner("3) find using $gte")
for d in col.find({"qty": {"$gte": 10}}):
    pprint(d)

banner("4) find using $eq")
for d in col.find({"name": {"$eq": "beta"}}):
    pprint(d)

banner("5) find using $ne")
for d in col.find({"name": {"$ne": "alpha"}}):
    pprint(d)

banner("6) find using $or")
for d in col.find({"$or": [{"qty": {"$lt": 10}}, {"name": "gamma"}]}):
    pprint(d)

banner("7) find using $and")
for d in col.find({"$and": [{"qty": {"$gte": 10}}, {"price": {"$lt": 30}}]}):
    pprint(d)

banner("8) find using $not")
for d in col.find({"qty": {"$not": {"$lt": 10}}}):
    pprint(d)

banner("9) find using $exists")
for d in col.find({"item": {"$exists": True}}):
    pprint(d)

banner("10) find using $elemMatch")
for d in col.find({"tags": {"$elemMatch": {"$eq": "blue"}}}):
    pprint(d)

banner("11) statement using $inc")
col.update_one({"name": "alpha"}, {"$inc": {"qty": 3}})
pprint(col.find_one({"name": "alpha"}))

banner("12) find using {item: null}")
for d in col.find({"item": None}):
    pprint(d)

banner("13) find using {item: {$exists: false}}")
for d in col.find({"item": {"$exists": False}}):
    pprint(d)

banner("14) find using {item: {$type: 10}}")
for d in col.find({"item": {"$type": 10}}):
    pprint(d)

banner("15) find using projection")
for d in col.find({}, {"name": 1, "qty": 1, "_id": 0}):
    pprint(d)

# part 2 – indexing
banner("part 2: indexing")

print("1) find without index")
res = col.find({"name": "alpha"})
for r in res:
    pprint(r)

print("2) explain showing no index")
pprint(col.find({"name": "alpha"}).explain()["queryPlanner"])

print("3) creating index")
col.create_index([("name", ASCENDING)])

print("4) explain showing index is used")
pprint(col.find({"name": "alpha"}).explain()["queryPlanner"])

print("5) dropping index")
col.drop_index("name_1")

# part 3 – menu app
banner("part 3: gadget menu")

def validate_int(prompt, low, high):
    while True:
        try:
            val = int(input(prompt))
            if val < low or val > high:
                print("out of range")
                continue
            return val
        except:
            print("enter a whole number")

def validate_float(prompt, low, high):
    while True:
        try:
            val = float(input(prompt))
            if val < low or val > high:
                print("out of range")
                continue
            return val
        except:
            print("enter a number")

def add_gadget():
    sku = input("sku: ")
    title = input("title: ")
    specs = {
        "weight": validate_float("weight (0.1-10): ", 0.1, 10),
        "life": validate_int("life (1-60): ", 1, 60),
        "power": validate_float("power (1-200): ", 1, 200)
    }
    gadgets.insert_one({"sku": sku, "title": title, "specs": specs})
    print("added")

def show_all():
    for g in gadgets.find({}):
        pprint(g)

def show_one():
    sku = input("enter sku: ")
    g = gadgets.find_one({"sku": sku})
    if g:
        pprint(g)
    else:
        print("not found")

def update_gadget():
    sku = input("sku to update: ")
    g = gadgets.find_one({"sku": sku})
    if not g:
        print("no match")
        return
    print("current specs:", g["specs"])
    new_specs = {
        "weight": validate_float("new weight (0.1-10): ", 0.1, 10),
        "life": validate_int("new life (1-60): ", 1, 60),
        "power": validate_float("new power (1-200): ", 1, 200)
    }
    gadgets.update_one({"sku": sku}, {"$set": {"specs": new_specs}})
    print("updated")

def delete_gadget():
    sku = input("sku to delete: ")
    gadgets.delete_one({"sku": sku})
    print("deleted if existed")

while True:
    print("\nmenu:")
    print("1 add gadget")
    print("2 display all")
    print("3 display one")
    print("4 update gadget")
    print("5 delete gadget")
    print("6 quit")
    choice = input("select: ")
    if choice == "1":
        add_gadget()
    elif choice == "2":
        show_all()
    elif choice == "3":
        show_one()
    elif choice == "4":
        update_gadget()
    elif choice == "5":
        delete_gadget()
    elif choice == "6":
        print("bye")
        break
    else:
        print("invalid")
