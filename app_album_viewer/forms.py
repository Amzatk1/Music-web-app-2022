from .models import Album, Comment  
from django.contrib.auth.forms import AuthenticationForm
from django import forms
#TO define form to help adding comments
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']  

#To define form for adding or editing albums
class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['cover', 'title', 'description', 'artist', 'price', 'format', 'release_date']

    #To define choices for "format" field
    FORMAT_CHOICES = [
        ('CD', 'CD'),
        ('Vinyl', 'Vinyl'),
        ('Digital', 'Digital'),
        
    ]

    format = forms.ChoiceField(choices=FORMAT_CHOICES, widget=forms.Select)
#To define a form for the user login
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
#To define a form to aid recommending an album to a friend
class RecommendForm(forms.Form):
    to_email = forms.EmailField(label="Friend's Email", required=True)
    title = forms.CharField(label="Album Title", required=True)
    message = forms.CharField(widget=forms.Textarea, label="Your Message", required=False)

    def set_initial_message(self, album):
        initial_message = f"Album special: '{album.title}' by {album.artist}. It's really worth a listen!"
        self.fields['message'].initial = initial_message