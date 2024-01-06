from django.urls import path

from app_book import views

urlpatterns = [
    path("authors", views.AuthorListView.as_view(), name="author-list"),
    path("authors/<int:obj_id>", views.AuthorDetailsView.as_view(), name="author-details"),
    path("authors/search", views.AuthorSearchView.as_view(), name="author-search"),
    path("books", views.BookListView.as_view(), name="book-list"),
    path("books/<int:obj_id>", views.BookDetailsView.as_view(), name="book-details"),
    path("books/search", views.BookSearchView.as_view(), name="book-search"),
    path("genres", views.GenreListView.as_view(), name="genre-list"),
    path("genres/<int:obj_id>", views.GenreDetailsView.as_view(), name="genre-details"),
    path("genres/search", views.GenreSearchView.as_view(), name="genre-search"),
    path("book-genres", views.BookGenreListView.as_view(), name="bookgenre-list"),
    path("book-genres/<int:obj_id>", views.BookGenreDetailsView.as_view(), name="bookgenre-details"),
    path("book-genres/search", views.BookGenreSearchView.as_view(), name="bookgenre-search"),
]