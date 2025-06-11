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
