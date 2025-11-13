from datetime import datetime, timedelta

class Borrower:
    def __init__(self, name, contact, membership_id):
        self.name = name
        self.contact = contact
        self.membership_id = membership_id
        self.borrowed_books = []

    def update_contact(self, new_contact):
        self.contact = new_contact

    def borrow_book(self, book):
        if book.is_available():
            book.quantity -= 1
            due_date = datetime.now() + timedelta(days=14)
            self.borrowed_books.append((book, due_date))
            print(f"Book borrowed successfully! Due Date: {due_date.date()}")
        else:
            print("Book not available.")

    def return_book(self, isbn):
        for book, due_date in self.borrowed_books:
            if book.isbn == isbn:
                book.quantity += 1
                self.borrowed_books.remove((book, due_date))
                print(f"Returned '{book.title}' successfully.")
                return
        print("No record of this book being borrowed.")

    def __str__(self):
        return f"{self.name} (ID: {self.membership_id}) | Contact: {self.contact}"
