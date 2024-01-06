from django.shortcuts import render
from app_book import models, serializers
from utility.views import BaseListView, BaseDetailsView, BaseSearchView


class AuthorListView(BaseListView):
    name = "Author list view"
    model = models.Author
    serializer = serializers.AuthorSerializer


class AuthorDetailsView(BaseDetailsView):
    name = "Author details view"
    model = models.Author
    serializer = serializers.AuthorSerializer


class AuthorSearchView(BaseSearchView):
    name = "Author search view"
    model = models.Author
    serializer = serializers.AuthorSerializer


class BookListView(BaseListView):
    name = "Book list view"
    model = models.Book
    serializer = serializers.BookSerializer


class BookDetailsView(BaseDetailsView):
    name = "Book details view"
    model = models.Book
    serializer = serializers.BookSerializer


class BookSearchView(BaseSearchView):
    name = "Book search view"
    model = models.Book
    serializer = serializers.BookSerializer


class GenreListView(BaseListView):
    name = "Genre list view"
    model = models.Genre
    serializer = serializers.GenreSerializer


class GenreDetailsView(BaseDetailsView):
    name = "Genre details view"
    model = models.Genre
    serializer = serializers.GenreSerializer


class GenreSearchView(BaseSearchView):
    name = "Genre search view"
    model = models.Genre
    serializer = serializers.GenreSerializer


class BookGenreListView(BaseListView):
    name = "BookGenre list view"
    model = models.BookGenre
    serializer = serializers.BookGenreSerializer


class BookGenreDetailsView(BaseDetailsView):
    name = "BookGenre details view"
    model = models.BookGenre
    serializer = serializers.BookGenreSerializer


class BookGenreSearchView(BaseSearchView):
    name = "BookGenre search view"
    model = models.BookGenre
    serializer = serializers.BookGenreSerializer
