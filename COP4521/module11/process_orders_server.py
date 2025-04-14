import socketserver
from encrypt import decrypt
from models import db, Customer, Order
from flask import Flask
from config import Config
from models import db, Customer, Order
from encrypt import decrypt

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
SEPARATOR = "^%$"

class OrderHandler(socketserver.BaseRequestHandler):
    def handle(self):
        encrypted_msg = self.request.recv(1024).decode('utf-8')
        print("Encrypted Message Received:", encrypted_msg)

        try:
            decrypted = decrypt(encrypted_msg)
            print("Decrypted:", decrypted)
            parts = decrypted.split(SEPARATOR)
            if len(parts) != 5:
                print("Incorrect number of fields.")
                return

            cust_id, sku, quantity, price, cc_num = parts
            with app.app_context():
                # Validate
                if not cust_id.isdigit() or int(cust_id) <= 0:
                    print("Invalid CustID")
                    return
                if not Customer.query.get(int(cust_id)):
                    print("CustID not found")
                    return
                if not sku.strip():
                    print("Invalid SKU")
                    return
                if not quantity.isdigit() or int(quantity) <= 0:
                    print("Invalid Quantity")
                    return
                try:
                    price = float(price)
                    if price <= 0:
                        print("Invalid Price")
                        return
                except:
                    print("Invalid Price Format")
                    return
                if not cc_num.strip():
                    print("Invalid Credit Card")

                # Create Order
                order = Order(
                    customer_id=int(cust_id),
                    item_sku=sku,
                    quantity=int(quantity),
                    price=price
                )
                order.set_credit_card_num(cc_num)
                db.session.add(order)
                db.session.commit()
                print(f"Record successfully added for custId: {cust_id}")

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    with app.app_context():
        print(f"Order processing server running on {HOST}:{PORT}")
        with socketserver.TCPServer((HOST, PORT), OrderHandler) as server:
            server.serve_forever()
