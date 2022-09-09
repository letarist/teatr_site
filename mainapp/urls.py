from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import PostDetail, contacts, genre, main

app_name = "mainapp"

urlpatterns = [
    path("", main, name="main"),
    path("contacts/", contacts, name="contacts"),
    path("<int:pk>/", genre, name="genre"),
    path("performance/<int:pk>/", PostDetail.as_view(), name="post_detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
