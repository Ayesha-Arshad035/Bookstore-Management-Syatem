class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.cart = {}      

    def display_user_info(self):
        print(f"Username : {self.username}")
        print(f"Email    : {self.email}")

    
    def add_to_cart(self, book, quantity=1):
     if quantity <= 0:
        print("Invalid quantity.")
        return
     if book.get_stock() >= quantity:
         if  book in self.cart:
            self.cart[book] += quantity
         else:
            self.cart[book] = quantity
         print(f"{quantity} of '{book.title}' added to cart.")
     else:
        print(f"Not enough stock")

    def remove_from_cart(self, book):
        if book in self.cart:
            del self.cart[book]
            print(f"Removed '{book.title}' from cart.")
        else:
            print(f"'{book.title}' is not in the cart.")

    def view_cart(self):
     if len(self.cart) == 0:
        print("Cart is empty.")
        return
     print("Shopping Cart:")
     total = 0.0  
     for book in self.cart:
        quantity = self.cart[book] 
        price_per_book = book.get_price()  
        subtotal = price_per_book * quantity  
        total = total + subtotal
        print(f"{book.title} by {book.author}")
        print(f"Quantity: {quantity}")
        print(f"Subtotal: ${subtotal:.2f}")
     print(f"Total Price: ${total:.2f}")