from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from .models import Album, Comment, Song
from django.contrib.auth.models import User
# Define test cases for the Album model
class AlbumModelTest(TestCase):
    cover_art_file_path = SimpleUploadedFile('dripping-stereo.png', b"file_content", content_type="image/png")

    def setUp(self):
        self.album = Album.objects.create(
            title="Test Album",
            artist="Test Artist",
            price=9.99,
            format="CD",
            release_date="2021-01-01",
            cover=self.cover_art_file_path  # Access the class attribute using self
        )

    def test_album_creation(self):
        # To confirm if the Album object is created successfully
        self.assertTrue(isinstance(self.album, Album))
        self.assertEqual(self.album.__str__(), self.album.title)
# To define test cases for the Comment 
class CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('testuser', 'test@example.com', 'testpassword')
        self.album = Album.objects.create(
            title="Test Album",
            artist="Test Artist",
            price=9.99,
            format="CD",
            release_date="2021-01-01"
        )
        self.comment = Comment.objects.create(
            album=self.album,
            user_display_name=self.user.username,
            message="Test comment"
        )

    def test_comment_creation(self):
        #to confim if the Comment object is created successfully
        self.assertTrue(isinstance(self.comment, Comment))
        self.assertEqual(self.comment.__str__(), f"{self.user.username} on {self.album.title}")

class ViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.album = Album.objects.create(
            title="Test Album",
            artist="Test Artist",
            price=9.99,
            format="CD",
            release_date="2021-01-01"
        )

    def test_album_list_view(self):
        response = self.client.get(reverse('albums'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.album.title, response.content.decode())

    def test_album_detail_view(self):
        response = self.client.get(reverse('album_info', args=[self.album.id]))
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.album.title, response.content.decode())


