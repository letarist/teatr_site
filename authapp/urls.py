from django.urls import path
from authapp.views import authentication, logout

app_name = 'authapp'
urlpatterns = [
    path('auth/', authentication, name='authentication'),
    path('logout/', logout, name='logout')
]
