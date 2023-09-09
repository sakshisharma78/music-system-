from django.shortcuts import render
from .models import Album, Song, Playlist

def home(request):
    albums = Album.objects.all()
    return render(request, 'musicapp/home.html', {'albums': albums})

def album_detail(request, album_id):
    album = Album.objects.get(pk=album_id)
    return render(request, 'musicapp/album_detail.html', {'album': album})

def playlist_detail(request, playlist_id):
    playlist = Playlist.objects.get(pk=playlist_id)
    return render(request, 'musicapp/playlist_detail.html', {'playlist': playlist})
