from django.urls import path

from .views import index, profile


app_name = 'profiles'
urlpatterns = [
    path('', index, name='index'),
    path('<str:username>/', profile, name='profile'),
]
