from django.urls import path
from . import views

app_name = 'musicapp'

urlpatterns = [
   
    path('', views.home, name='home'),
   
    path('album/<int:album_id>/', views.album_details, name='album_details'),
    path('playlist/<int:playlist_id>/', views.playlist_details, name='playlist_details'),
]
