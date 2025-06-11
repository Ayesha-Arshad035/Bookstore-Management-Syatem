from book import Book
from user import User

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