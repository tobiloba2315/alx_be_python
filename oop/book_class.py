class Book:
    def __init__(self, title, author, year):
        """Initialize a Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Print a message when a Book object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Readable string representation of the Book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation that can recreate the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
    def get_summary(self):
        """Return a summary of the book."""
        return f"'{self.title}' is a book written by {self.author} in {self.year}."
    def is_classic(self):
        """Determine if the book is a classic (published more than 50 years ago)."""
        current_year = 2024
        return (current_year - self.year) > 50
    def age(self):
        """Return the age of the book."""
        current_year = 2024
        return current_year - self.year
    def update_year(self, new_year):
        """Update the publication year of the book."""
        self.year = new_year