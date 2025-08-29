from django.contrib import admin
from .models import Book

# Register the Book model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # columns to display in list view
    search_fields = ('title', 'author')  # add search capability
    list_filter = ('publication_year',)  # add filter options

