import csv

from django.core.management import BaseCommand, CommandError, call_command


from app_book.models import Genre, Author, Book, BookGenre
from app_auth.serializers import UserSerializer


class Command(BaseCommand):

    def create_genre(self, genre_name: str):
        if not Genre.objects.filter(name=genre_name.lower().strip()).exists():
            genre = Genre(name=genre_name.lower())
            genre.save()
            return genre
        return Genre.objects.filter(name=genre_name.lower().strip()).first()

    def create_author(self, author_name: str):
        if not Author.objects.filter(name=author_name).exists():
            author = Author(name=author_name)
            author.save()
            return author
        return Author.objects.filter(name=author_name).first()

    def process_entry(self, entry):
        genres = entry["genre1"].split(",") + entry["genre2"].split(",")
        genre_ids = []
        for i in genres:
            genre_ids.append(self.create_genre(i).id)
        author_id = self.create_author(entry["author"]).id
        book = Book(title=entry["title"], author_id=author_id)
        book.save()
        book_genres = []
        for i in genre_ids:
            book_genres.append(BookGenre(book_id=book.id, genre_id=i))
        BookGenre.objects.bulk_create(book_genres)

    def handle(self, *args, **options):
        call_command("flush", "--verbosity=1", "--no-input")

        data = csv.DictReader(
            open(f"./app_data/dummydata/raw_data.csv", "r"), delimiter=","
        )

        for i in data:
            self.stdout.write(f"Processing {i}",ending="\n")
            self.process_entry(i)

        data = csv.DictReader(open(f"./app_data/dummydata/users.csv"))
        for i in data:
            user = UserSerializer(data=i)
            if user.is_valid():
                user.save()
            else:
                self.stdout.write(str(user.errors), ending="\n")

