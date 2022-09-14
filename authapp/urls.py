from django.urls import path
from authapp.views import authentication, logout, profile, register

app_name = 'authapp'
urlpatterns = [
    path('auth/', authentication, name='authentication'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('register/', register, name='register'),
]
