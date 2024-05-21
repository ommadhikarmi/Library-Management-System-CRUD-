from django.contrib import admin
from.models import Category
from.models import Authors
from.models import Book
from.models import BookFile
# Register your models here.
admin.site.register(Category)
admin.site.register(Authors)
admin.site.register(Book)
admin.site.register(BookFile)
