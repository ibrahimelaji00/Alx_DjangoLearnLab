
from django.contrib import admin
from .models import Book

# Basic registration
# admin.site.register(Book)

# Custom admin configuration
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # columns to show in admin
    search_fields = ('title', 'author')                     # allow search by title or author
    list_filter = ('publication_year',)                     # filter by publication year

admin.site.register(Book, BookAdmin)
