from datetime import datetime
from src.book import Book
from src.borrower import Borrower

class Library:
    def __init__(self):
        self.books = []
        self.borrowers = []

    #Book Management
    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added.")

    def update_book(self, isbn, **kwargs):
        book = self.find_book(isbn)
        if book:
            book.update_details(**kwargs)
            print("Book updated.")
        else:
            print("Book not found.")

    def remove_book(self, isbn):
        book = self.find_book(isbn)
        if book:
            self.books.remove(book)
            print("Book removed.")
        else:
            print("Book not found.")

    # Borrower Management
    def add_borrower(self, borrower):
        self.borrowers.append(borrower)
        print("Borrower added.")

    def update_borrower(self, membership_id, new_contact):
        borrower = self.find_borrower(membership_id)
        if borrower:
            borrower.update_contact(new_contact)
            print("Borrower updated.")
        else:
            print("Borrower not found.")

    def remove_borrower(self, membership_id):
        borrower = self.find_borrower(membership_id)
        if borrower:
            self.borrowers.remove(borrower)
            print("Borrower removed.")
        else:
            print("Borrower not found.")

    #Borrow/Return
    def borrow_book(self, membership_id, isbn):
        borrower = self.find_borrower(membership_id)
        book = self.find_book(isbn)
        if borrower and book:
            borrower.borrow_book(book)
        else:
            print("Borrower or book not found.")

    def return_book(self, membership_id, isbn):
        borrower = self.find_borrower(membership_id)
        if borrower:
            borrower.return_book(isbn)
        else:
            print("Borrower not found.")

    # Search
    def search_books(self, keyword):
        keyword = keyword.lower()
        results = [b for b in self.books if keyword in b.title.lower() or keyword in b.author.lower() or keyword in b.genre.lower()]
        if results:
            print("\nSearch Results:")
            for b in results:
                print(f"- {b}")
        else:
            print("No books found.")

    #Overdue
    def show_overdue(self):
        today = datetime.now()
        for borrower in self.borrowers:
            for book, due_date in borrower.borrowed_books:
                if due_date < today:
                    print(f"{book.title} borrowed by {borrower.name} is overdue!")

    # Helpers
    def find_book(self, isbn):
        return next((b for b in self.books if b.isbn == isbn), None)

    def find_borrower(self, membership_id):
        return next((b for b in self.borrowers if b.membership_id == membership_id), None)
