from django.contrib import admin
from app_book import models

admin.site.register(models.Author)
admin.site.register(models.Book)
admin.site.register(models.Genre)
admin.site.register(models.BookGenre)