# library management.py 

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def checkout(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        """Mark the book as returned if it is checked out."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book.check_out()
                return f"Checked out: {title}"
        return f"{title} is unavailable."
    
    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book.return_book()
                return f"Returned: {title}"
        return f"{title} is not checked out."
    
    def list_available_books(self):
        available_books = [book for book in self._books if not book._is_checked_out]
        for book in available_books:
            print(f"{book.title} by {book.author}")
