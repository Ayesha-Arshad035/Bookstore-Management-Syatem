from book import Book
from BookStore import Bookstore
from customer import Customer
from admin import Admin

def display_menu():
    print("\n===== Online Bookstore Menu =====")
    print("1. Login")
    print("2. Search Books")
    print("3. View Cart")
    print("4. Place Order")
    print("5. Logout")
    print("0. Exit")

if __name__ == "__main__":
    # Existing setup
    store = Bookstore("Online Bookstore Management System")

    book1 = Book("Physics", "John Doe", "ISBN001", 29.99, 10)
    book2 = Book("Chemistry", "Jane Smith", "ISBN002", 39.99, 5)
    store.add_book_to_catalog(book1)
    store.add_book_to_catalog(book2)

    customer = Customer("Ayesha", "password12345", "xyz@gmail.com", "Hyderabad")
    admin = Admin("admin", "root123", "admin@store.com")
    store.register_user(customer)
    store.register_user(admin)

    current_user = None

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Username: ")
            password = input("Password: ")
            current_user = store.login_user(username, password)

        elif choice == "2":
            if current_user:
                query = input("Enter book title or author to search: ")
                results = store.search_book(query)
                if results:
                    for i, book in enumerate(results, 1):
                        print(f"\nResult #{i}")
                        book.display_book_info()
                        add = input("Add this book to cart? (y/n): ")
                        if add.lower() == 'y':
                            qty = int(input("Enter quantity: "))
                            current_user.add_to_cart(book, qty)
                else:
                    print("No books found.")
            else:
                print("Please login first.")

        elif choice == "3":
            if current_user:
                current_user.view_cart()
            else:
                print("Please login first.")

        elif choice == "4":
            if current_user:
                order = current_user.place_order(store)
                if order:
                    order.display_order_details()
            else:
                print("Please login first.")

        elif choice == "5":
            current_user = None
            print("Logged out.")

        elif choice == "0":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")
