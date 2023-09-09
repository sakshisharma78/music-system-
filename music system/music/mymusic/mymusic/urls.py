from django.urls import path
from . import views

app_name = 'musicapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('album/<int:album_id>/', views.album_detail, name='album_detail'),
    path('playlist/<int:playlist_id>/', views.playlist_detail, name='playlist_detail'),
]
