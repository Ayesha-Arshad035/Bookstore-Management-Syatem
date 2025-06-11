from user import User
from order import Order
class Customer(User):
    def __init__(self, username, password, email, shipping_address):
        super().__init__(username, password, email)
        self.shipping_address = shipping_address
        self.order_history = []

    def place_order(self, bookstore):
        if not self.cart:
            print("Your cart is empty.")
            return None

        order = Order(self, self.cart)
        self.order_history.append(order)
        bookstore.process_order(order)

   
        for book, qty in self.cart.items():
            book.decrease_stock(qty)

        self.cart = {}   
        print("Order placed successfully.")
        return order
