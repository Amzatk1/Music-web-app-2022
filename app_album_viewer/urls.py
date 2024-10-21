from django.urls import path
from . import views

# Define URL patterns for the app
urlpatterns = [


    # URL pattern to display all albums
    path('albums/', views.albums, name='albums'),

    # URL pattern for editing an album by its ID(identification)
    path('edit_album/<int:id>/', views.edit_album, name='edit_album'),

    # URL pattern for deleting an album by its ID(identification)
    path('delete_album/<int:id>/', views.delete_album, name='delete_album'),

    
  
    # URL pattern for creating a new album
    path('create_album/', views.create_album, name='create_album'),

    # URL pattern for displaying album details by its ID
    path('albums/<int:id>/', views.album_info, name='album_info'),

]