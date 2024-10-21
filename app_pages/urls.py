


from django.urls import path
from . import views
from .views import user_logout 

# Define URL patterns for the app
urlpatterns = [



    # URL pattern for the About page
    path('about/', views.about, name='about'),

       # URL pattern to user account page
    path('account/', views.account, name='account'),

        # URL pattern for the Contact page
    path('contact/', views.contact, name='contact'),

        # URL pattern to home page
    path('', views.home, name='home'),

    # URL pattern to login page
    path('login/', views.login_view, name='login'),

    # URL pattern to logout page
    path('logout/', user_logout, name='logout'),

    # URL pattern for recommending an album to a friend
    path('recommend_friend/<int:album_id>/', views.recommend_album, name='recommend_album'),]