from django.contrib import admin
from .models import Book, Publication

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'publication')
    search_fields = ('title', 'author')
    list_filter = ('publication',)

admin.site.register(Publication)
admin.site.register(Book, BookAdmin)
