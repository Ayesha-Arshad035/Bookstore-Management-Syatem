from datetime import datetime
import uuid
class Order:
    def __init__(self, customer, cart_items):
        self.order_id = str(uuid.uuid4())[:8]
        self.customer = customer
        self.items = [{"book": book, "quantity": qty} for book, qty in cart_items.items()
        ]
        self.total_amount = sum(item["book"].get_price() * item["quantity"] for item in self.items
        )
        self.order_date = datetime.now()
        self.status = "Pending"

    def display_order_details(self):       
        print(f"Order ID : {self.order_id}")
        print(f"Customer : {self.customer.username}")
        print(f"Date     : {self.order_date}")
        print(f"Status   : {self.status}")
        

    def update_status(self, new_status):
        self.status = new_status
        print(f"Order status updated to '{new_status}'.")
