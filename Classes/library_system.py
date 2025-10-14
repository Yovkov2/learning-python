
class Book:
    def __init__(self, title, author, pages):

        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        """Human-readable representation shown by print(book)."""
        return f"📘 '{self.title}' by {self.author} ({self.pages} pages)"

    def __len__(self):
        """Allows len(book) → returns number of pages."""
        return self.pages


class Library:
    def __init__(self, name):
        """
        Initialize an empty library.
        :param name: str - library name
        """
        self.name = name
        self.books = []  # list[Book]

    def add_book(self, book):
        """Add a Book instance to the collection."""
        if not isinstance(book, Book):
            raise TypeError("Only Book instances can be added.")
        self.books.append(book)
        print(f"✅ Added: {book}")

    def show_books(self):
        """Print all books in a friendly format."""
        if not self.books:
            print("The library is empty.")
            return
        print(f"\n🏛️ {self.name} — {len(self)} books:")
        for i, book in enumerate(self.books, start=1):
            print(f"{i}. {book}")

    def find_by_author(self, author):
        """Return a list of books written by the given author (case-insensitive)."""
        author_lower = author.lower()
        return [b for b in self.books if b.author.lower() == author_lower]

    def total_pages(self):
        """Total number of pages across all books."""
        return sum(len(b) for b in self.books)

    def __len__(self):
        """Allows len(library) → number of books."""
        return len(self.books)


if __name__ == "__main__":
    # Create some books
    b1 = Book("Clean Code", "Robert C. Martin", 464)
    b2 = Book("Automate the Boring Stuff with Python", "Al Sweigart", 592)
    b3 = Book("Python Crash Course", "Eric Matthes", 544)
    b4 = Book("Clean Architecture", "Robert C. Martin", 432)

    # Create a library and add books
    lib = Library("Python Dev Library")
    lib.add_book(b1)
    lib.add_book(b2)
    lib.add_book(b3)
    lib.add_book(b4)

    # Show catalog
    lib.show_books()

    # Queries
    print("\n🔎 Books by Robert C. Martin:")
    for bk in lib.find_by_author("Robert C. Martin"):
        print(" -", bk)

    print(f"\n📄 Total pages in library: {lib.total_pages()}")