from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from app_album_viewer.forms import UserLoginForm, RecommendForm
from app_album_viewer.models import Album, Comment
from django.shortcuts import render, redirect, get_object_or_404

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def home(request):
    return render(request, 'home.html')

def account(request):
    if request.user.is_authenticated:
        comments = Comment.objects.filter(user_display_name=request.user.username)
        return render(request, 'account.html', {'comments': comments})
    else:
        return redirect('login')  

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('home')  

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, request.POST)
		
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            print(f'Username: {username}, Password: {password}, User: {user}')

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid login credentials. Please try again.')
    else:
        form = UserLoginForm(request)

    return render(request, 'login.html', {'form': form})

def recommend_album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    if request.method == 'POST':
        form = RecommendForm(request.POST)
        if form.is_valid():
            to_email = form.cleaned_data['to_email']
            title = form.cleaned_data['title']
            message = form.cleaned_data['message']

            print("Sending recommendation email:")
            print(f"To: {to_email}")
            print(f"Subject: {title}")
            print(f"Message: {message}")

            return redirect('home')
    else:
        initial_message = f"Listen In To This Brilliant Album! '{album.title}' by {album.artist}. I think you'll love it!"
        form = RecommendForm(initial={'title': album.title, 'message': initial_message})

    return render(request, 'send_recommendation.html', {'form': form, 'album': album})