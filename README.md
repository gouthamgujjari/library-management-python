Library Management System (Python OOP)

A simplified console-based Library Management System built using Python Object-Oriented Programming (OOP) concepts.
This project supports book management, borrower management, borrowing/returning, search, and overdue tracking, using in-memory data structures without a database.

This assignment matches the structure required by VENHAN Backend Assignment.

Features
Book Management

Add new books

Update book details

Remove books

Check availability

Search by title/author/genre

Borrower Management

Add borrowers

Update borrower info

Remove borrowers

Track borrowed books

Borrowing & Returning

Borrow books (checks availability)

Auto-assign 14-day due date

Return books

Track overdue books

Search

Search books with keyword

Case-insensitive

Shows availability

Project Structure
library-management-python/
├── src/
│   ├── __init__.py
│   ├── book.py
│   ├── borrower.py
│   ├── library.py
├── main.py
├── README.md
└── .gitignore

* File Responsibilities
File	Purpose
book.py	Book class (title, author, genre, ISBN, quantity)
borrower.py	Borrower class (name, contact, borrowed books)
library.py	Main manager: books, borrowers, borrow/return logic
main.py	Menu-driven user interface for console
__init__.py	Makes src/ a Python package
.gitignore	Ignores cache files
* OOP Concepts Used
Concept	Usage
Encapsulation	Book, Borrower, Library classes hold their own data & methods
Abstraction	Library exposes simple methods: borrow, return, search
Polymorphism	Methods update behavior based on data (e.g., availability)
Modularity	Code split into multiple reusable classes