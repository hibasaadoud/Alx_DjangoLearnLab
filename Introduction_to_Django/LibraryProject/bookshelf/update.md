# Update Operation

```python
from bookshelf.models import Book
Book.objects.filter(title="1984").update(title="Nineteen Eighty-Four")
book = Book.objects.get(title="Nineteen Eighty-Four")
book
# Output: <Book: Nineteen Eighty-Four>


