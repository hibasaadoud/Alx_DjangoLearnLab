import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def prepare_sample_data():
    # Create an author and two books
    author, _ = Author.objects.get_or_create(name="George Orwell")

    book1, _ = Book.objects.get_or_create(title="1984", author=author)
    book2, _ = Book.objects.get_or_create(title="Animal Farm", author=author)

    # Create a library and add books
    library, _ = Library.objects.get_or_create(name="Central Library")
    library.books.add(book1, book2)

    # Create a librarian linked one-to-one to the library
    librarian, _ = Librarian.objects.get_or_create(name="Alice", library=library)

    return author, [book1, book2], library, librarian

def run_queries():
    author, books, library, librarian = prepare_sample_data()

    # Query 1: Query all books by a specific author
    books_by_author = Book.objects.filter(author=author)
    print("Books by author", author.name, ":", [b.title for b in books_by_author])

    # Query 2: List all books in a library
    library_books = library.books.all()
    print("Books in library", library.name, ":", [b.title for b in library_books])

    # Query 3: Retrieve the librarian for a library
    lib_librarian = library.librarian  # OneToOne relation
    print("Librarian for library", library.name, ":", lib_librarian.name)

if __name__ == "__main__":
    run_queries()

