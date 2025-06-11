from book import Book
from BookStore import Bookstore
from customer import Customer
from admin import Admin


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
    for b in store.search_book("Physics"):
            b.display_book_info()
    user.add_to_cart(book1, 2)
    user.view_cart()
    order = user.place_order(store)
    order.display_order_details()
    admin_user = store.login_user("admin", "root123")
    admin_user.view_all_users(store)
    admin_user.add_book(store, "Biology", "Dr. Akhtar", "ISBN007", 49.99, 8)
    admin_user.update_book_stock(store, "ISBN007", 15)
    order.update_status("Shipped")
