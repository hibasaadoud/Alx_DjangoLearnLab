# Update Operation

```python
from bookshelf.models import Book

# Retrieve the book first
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Confirm the update
book.title
# Output: 'Nineteen Eighty-Four'


