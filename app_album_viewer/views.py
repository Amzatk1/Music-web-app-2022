from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Album, Comment, Song  
from .forms import CommentForm
from .forms import AlbumForm 
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import UserLoginForm  # to import login info 
from django.db.models import Count



def album_info(request, id):
    album = get_object_or_404(Album, id=id)
    songs_with_duration = Song.objects.filter(albums__id=id)
    comments = Comment.objects.filter(album=album)
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.album = album
            comment.user_display_name = request.user.username
            comment.save()
            return redirect('album_info', id=id)
    else:
        comment_form = CommentForm()

    return render(request, 'album_info.html', {
        'album': album,
        'songs_with_duration': songs_with_duration,
        'comments': comments,
        'comment_form': comment_form,
    })

def albums(request):
    albums = Album.objects.annotate(num_comments=Count('comment'))
    return render(request, 'albums.html', {'albums': albums})


def edit_album(request, id):
    # Retrieve the album object based on the provided ID
    album = get_object_or_404(Album, id=id)

    if request.method == 'POST':
        # If the form is submitted, update the album with the new data
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album_info', id=id)  
    else:
        # If the request is GET, populate the form with the album data present
        form = AlbumForm(instance=album)

    return render(request, 'edit_album.html', {'form': form, 'album': album})

def delete_album(request, id):
    # To help retrieve the album object based on the provided Identification
    album = get_object_or_404(Album, id=id)

    if request.method == 'POST':
        # If the delete form is submitted, delete the album
        album.delete()
        return redirect('albums') 
    return render(request, 'delete_album.html', {'album': album})



def create_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the new album to the database
            return redirect('albums')  # Redirect to the album list page or any other page
    else:
        form = AlbumForm()

    return render(request, 'create_album.html', {'form': form})