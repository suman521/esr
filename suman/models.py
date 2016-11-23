from django.db import models

# Create your models here.
class Album(models.Model):
    artist=models.CharField(max_length=250)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    artist_name = models.CharField(max_length=250)
class Song(models.Model):
    album=models.ForeignKey(Album, on_delete=models.CASCADE)
    sing_title = models.CharField(max_length=250)
    file_type = models.CharField(max_length=250)
    song_name = models.CharField(max_length=250)