from src.book import Book
from src.borrower import Borrower
from src.library import Library

def main():
    library = Library()

    while True:
        print("\n===== LIBRARY MENU =====")
        print("1. Add Book")
        print("2. Add Borrower")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Search Books")
        print("6. Show Overdue")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            genre = input("Genre: ")
            qty = int(input("Quantity: "))
            library.add_book(Book(title, author, isbn, genre, qty))

        elif choice == "2":
            name = input("Name: ")
            contact = input("Contact: ")
            member_id = input("Membership ID: ")
            library.add_borrower(Borrower(name, contact, member_id))

        elif choice == "3":
            mid = input("Membership ID: ")
            isbn = input("ISBN: ")
            library.borrow_book(mid, isbn)

        elif choice == "4":
            mid = input("Membership ID: ")
            isbn = input("ISBN: ")
            library.return_book(mid, isbn)

        elif choice == "5":
            keyword = input("Enter search keyword: ")
            library.search_books(keyword)

        elif choice == "6":
            library.show_overdue()

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
