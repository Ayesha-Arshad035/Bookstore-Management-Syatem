from datetime import datetime
import uuid
##Part 1: Core Classes
class Book:
    def __init__(self, title, author, isbn, price, stock):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price
        self.stock = stock

    def display_book_info(self):
        print(f"Title of the book  : {self.title}")
        print(f"Author of the book : {self.author}")
        print(f"ISBN of the book   : {self.isbn}")
        print(f"Price of the book  : ${self.price}")
        print(f"Stock of the book : {self.stock}")

    def get_price(self):
        return self.price

    def get_stock(self):
        return self.stock

    def decrease_stock(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
        else:
            print("Not enough stock available.")

    def increase_stock(self, quantity):
        self.stock += quantity


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

## Part 2: Inheritance- Specialized User
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


class Admin(User):
 
    def add_book(self, bookstore, title, author, isbn, price, stock):
        book = Book(title, author, isbn, price, stock)
        bookstore.add_book_to_catalog(book)
        print(f"Book '{title}' added to catalog.")

    def remove_book(self, bookstore, isbn):
        bookstore.remove_book_from_catalog(isbn)

    def update_book_stock(self, bookstore, isbn, new_stock):
        if isbn in bookstore.book_catalog:
            bookstore.book_catalog[isbn].stock = new_stock
            print(f"Stock updated for ISBN {isbn}.")
        else:
            print("Book not found.")

    def view_all_users(self, bookstore):
        for user in bookstore.registered_users.values():
            user.display_user_info()

## Part 3: Association - Order Management
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

## Part 4: Aggregation/Composition - The Bookstore Itself
class Bookstore:
    def __init__(self, name):
        self.name = name
        self.book_catalog = {}      
        self.registered_users = {}  
        self.orders = []            


    def register_user(self, user):
        self.registered_users[user.username] = user
        print(f"User '{user.username}' registered successfully.")

    def login_user(self, username, password):
        user = self.registered_users.get(username)
        if user and user.password == password:
            print(f"User '{username}' logged in successfully.")
            return user
        print("Login failed.")
        return None

  
    def search_book(self, query, search_by="title"):
        results = []
        for book in self.book_catalog.values():
            if search_by == "title" and query.lower() in book.title.lower():
                results.append(book)
            elif search_by == "author" and query.lower() in book.author.lower():
                results.append(book)
        return results

    def add_book_to_catalog(self, book):
        self.book_catalog[book.isbn] = book

    def remove_book_from_catalog(self, isbn):
        if isbn in self.book_catalog:
            del self.book_catalog[isbn]
            print(f"Book with ISBN {isbn} removed.")
        else:
            print("Book not found.")

 
    def process_order(self, order):
        self.orders.append(order)


## Part 5: Putting It All Together - Simulation and Interaction
if __name__ == "__main__":
    ## 1. Create a Bookstore instance.
    store = Bookstore("Online Bookstore Management System")

    ## 2. Add a few initial Book objects to the bookstore's catalog.
    book1 = Book("Physics", "John Doe", "ISBN001", 29.99, 10)
    book2 = Book("Chemistry", "Jane Smith", "ISBN002", 39.99, 5)
    book3 = Book("Maths", "Albert Newton", "ISBN003", 24.99, 8)
    book4 = Book("English", "Emily Bronte", "ISBN004", 19.99, 12)
    book5 = Book("General Knowledge", "Isaac Trivia", "ISBN005", 14.99, 20)
    book6 = Book("Arts", "Leonardo Vinci", "ISBN006", 34.99, 7)


    for bk in (book1, book2, book3, book4, book5, book6):
        store.add_book_to_catalog(bk)

    ## 3. Register a Customer and an Admin user.
    customer = Customer("Ayesha", "password12345", "xyz@gmail.com", "Hyderabad")
    admin = Admin("admin", "root123", "admin@store.com")
    store.register_user(customer)
    store.register_user(admin)
   
    ## 4. Demonstrate the following interactions:
    user = store.login_user("Ayesha", "password12345")
  
    if user:
        for b in store.search_book("Physics"):
            b.display_book_info()
   
        user.add_to_cart(book1, 2)
   
        user.view_cart()

        order = user.place_order(store)

        if order:
            order.display_order_details()

 
    admin_user = store.login_user("admin", "root123")

    if admin_user:
        admin_user.view_all_users(store)

        admin_user.add_book(store, "Biology", "Dr. Akhtar", "ISBN007", 49.99, 8)

        admin_user.update_book_stock(store, "ISBN007", 15)
        
        order.update_status("Shipped")
