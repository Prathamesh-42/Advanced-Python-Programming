# Book Class
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        self.is_borrowed = False


# Patron Class
class Patron:
    def __init__(self, name, patron_id):
        self.name = name
        self.patron_id = patron_id
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)


# Library Class
class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    # Add a new book
    def add_book(self, book):
        self.books.append(book)

    # Register a new patron
    def register_patron(self, patron):
        self.patrons.append(patron)

    # Borrow a book
    def borrow_book(self, patron_id, isbn):
        patron = None
        book = None

        for p in self.patrons:
            if p.patron_id == patron_id:
                patron = p
                break

        for b in self.books:
            if b.isbn == isbn:
                book = b
                break

        if patron and book:
            if book.borrow():
                patron.borrow_book(book)
                print(f"{patron.name} borrowed '{book.title}'.")
            else:
                print("Book is already borrowed.")
        else:
            print("Book or Patron not found.")

    # Return a book
    def return_book(self, patron_id, isbn):
        patron = None
        book = None

        for p in self.patrons:
            if p.patron_id == patron_id:
                patron = p
                break

        for b in self.books:
            if b.isbn == isbn:
                book = b
                break

        if patron and book:
            patron.return_book(book)
            book.return_book()
            print(f"{patron.name} returned '{book.title}'.")
        else:
            print("Book or Patron not found.")

    # Display all books
    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books:
            status = "Borrowed" if book.is_borrowed else "Available"
            print(f"{book.title} by {book.author} | ISBN: {book.isbn} | {status}")

    # Display all patrons
    def display_patrons(self):
        print("\nRegistered Patrons:")
        for patron in self.patrons:
            print(f"Name: {patron.name}, ID: {patron.patron_id}")
            if patron.borrowed_books:
                print("Borrowed Books:")
                for book in patron.borrowed_books:
                    print(" -", book.title)
            else:
                print("No books borrowed.")


# ---------------- Main Program ----------------

library = Library()

# Add Books
book1 = Book("Python Programming", "Guido van Rossum", "101")
book2 = Book("Data Structures", "Mark Allen", "102")
book3 = Book("Machine Learning", "Andrew Ng", "103")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Register Patrons
patron1 = Patron("Rahul", 1)
patron2 = Patron("Priya", 2)

library.register_patron(patron1)
library.register_patron(patron2)

# Display Books
library.display_books()

# Borrow Books
library.borrow_book(1, "101")
library.borrow_book(2, "102")

# Display Information
library.display_books()
library.display_patrons()

# Return Book
library.return_book(1, "101")

# Final Display
library.display_books()
library.display_patrons()