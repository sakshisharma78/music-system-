from django.db import models
from django.contrib.auth.models import User

class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='covers/')
    release_date = models.DateField()

class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='songs/')
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

class Playlist(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song)
