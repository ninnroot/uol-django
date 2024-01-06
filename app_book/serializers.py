from utility.serializers import BaseModelSerializer
from app_book import models


class AuthorSerializer(BaseModelSerializer):
    class Meta:
        model = models.Author
        fields = "__all__"
        expandable_fields = {
            "books": "app_book.serializers.BookSerializer"
        }


class BookSerializer(BaseModelSerializer):
    class Meta:
        model = models.Book
        fields = "__all__"
        expandable_fields = {
            "author": "app_book.serializers.AuthorSerializer",
            "book_genres": "app_book.serializers.BookGenreSerializer"
        }


class GenreSerializer(BaseModelSerializer):
    class Meta:
        model = models.Genre
        fields = "__all__"
        expandable_fields = {
            "book_genres": "app_book.serializers.BookGenreSerializer"
        }


class BookGenreSerializer(BaseModelSerializer):
    class Meta:
        model = models.BookGenre
        fields = "__all__"
        expandable_fields = {
            "book": "app_book.serializers.BookSerializer",
            "genre": "app_book.serializers.GenreSerializer"
        }
