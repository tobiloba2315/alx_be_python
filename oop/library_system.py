# Base Class - Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


# Derived Class - EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)  # Call base class constructor
        self.file_size = file_size      # Additional attribute unique to EBook


# Derived Class - PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)  # Call base class constructor
        self.page_count = page_count     # Additional attribute unique to PrintBook


# Composition - Library class
class Library:
    def __init__(self):
        self.books = []  # A list to store Book, EBook, and PrintBook objects

    def add_book(self, book):
        """Adds a book to the library"""
        self.books.append(book)

    def list_books(self):
        """Prints details of each book in the library"""
        for book in self.books:
            if isinstance(book, EBook):
                print(f"E-Book: {book.title} by {book.author}, File Size: {book.file_size}MB")
            elif isinstance(book, PrintBook):
                print(f"Print Book: {book.title} by {book.author}, Pages: {book.page_count}")
            else:
                print(f"Book: {book.title} by {book.author}")
