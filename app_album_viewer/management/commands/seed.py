from django.core.management.base import BaseCommand
import json
from django.contrib.auth.models import User

from app_album_viewer.models import Album, Song, Comment  # Update with your app's name and model paths


class Command(BaseCommand):
    help = 'Load data from a JSON file into the database'

    def handle(self, *args, **kwargs):
        json_file = 'sample_data/sample_data.json'  # Update with the path to your JSON file
        try:
            with open(json_file, 'r') as file:
                data = json.load(file)

            self.stdout.write("Loading users...")
            self.load_users(data['albums'])

            self.stdout.write("Loading albums and songs...")
            self.load_albums(data['albums'])
            self.load_songs(data.get('songs', []))

            self.stdout.write(self.style.SUCCESS('Database successfully seeded.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error occurred: {e}'))

    def load_users(self, albums_data):
        user_names = set()
        for album_data in albums_data:
            for comment_data in album_data.get('comments', []):
                display_name = comment_data.get('user__display_name', 'Unknown User')
                if display_name not in user_names:
                    user_names.add(display_name)
                    self.create_user(display_name)

    def create_user(self, display_name):
        email = f"{display_name.lower().replace(' ', '')}@example.com"
        password = 'password'
        user, created = User.objects.get_or_create(username=display_name, email=email)
        if created:
            user.set_password(password)
            user.save()

    def load_albums(self, albums_data):
        for album_data in albums_data:
            album, created = Album.objects.get_or_create(
                title=album_data['title'],
                defaults={
                    'cover': album_data['cover'],
                    'description': album_data['description'],
                    'artist': album_data['artist'],
                    'price': album_data['price'],
                    'format': album_data['format'],
                    'release_date': album_data['release_date'],
                }
            )
            self.load_comments(album, album_data.get('comments', []))

    def load_comments(self, album, comments_data):
        for comment_data in comments_data:
            user_display_name = comment_data.get('user__display_name', 'Unknown User')
            Comment.objects.create(
                album=album,
                user_display_name=user_display_name,
                message=comment_data['message']
            )

    def load_songs(self, songs_data):
        for song_data in songs_data:
            song, created = Song.objects.get_or_create(
                title=song_data['title'],
                runtime=song_data['runtime']
            )
            for album_title in song_data['albums']:
                album = Album.objects.get(title=album_title)
                song.albums.add(album)
