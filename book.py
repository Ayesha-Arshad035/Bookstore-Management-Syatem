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
