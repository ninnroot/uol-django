from django.db import models
from utility.models import BaseModel


class Author(BaseModel):
    name = models.CharField(max_length=5000)

    def __str__(self):
        return f"<{self.id}> {self.name}"


class Book(BaseModel):
    title = models.CharField(max_length=5000)
    description = models.TextField(null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="authors")

    def __str__(self):
        return f"<{self.id}> {self.title}"


class Genre(BaseModel):
    name = models.CharField(max_length=5000)

    def __str__(self):
        return f"<{self.id}> {self.name}"


class BookGenre(BaseModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="book_genres")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name="book_genres")

    def __str__(self):
        return f"<{self.id}> book_id={self.book_id}, genre_id={self.genre_id}"
