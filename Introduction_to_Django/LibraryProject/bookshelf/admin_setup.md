# Django Admin Setup for Book Model

- Registered the `Book` model in `bookshelf/admin.py`.
- Customized `BookAdmin` to display `title`, `author`, and `publication_year`.
- Added search fields for `title` and `author`.
- Added list filter for `publication_year`.

```python
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)

