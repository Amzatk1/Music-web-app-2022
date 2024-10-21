from django.db import models

from django.db import models
from django.contrib.auth.models import User
#To define the Album model
class Album(models.Model):
    title = models.CharField(max_length=255)
    cover = models.ImageField(upload_to='album_covers/', blank=True, null=True)

    description = models.TextField()
    artist = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    format = models.CharField(max_length=50)
    release_date = models.DateField()

    def __str__(self):
        return self.title
#To define the Comment model
class Comment(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    user_display_name = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return f"{self.user_display_name} on {self.album.title}"
#To define the Song model
class Song(models.Model):
    title = models.CharField(max_length=255)
    runtime = models.IntegerField()
    albums = models.ManyToManyField(Album, related_name='songs')

    def __str__(self):
        return self.title
 


        

