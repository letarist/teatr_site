from django.contrib import admin
from mainapp.models import Artist, Contact, Genre, Repertoire

admin.site.register(Artist)
admin.site.register(Genre)
admin.site.register(Repertoire)
admin.site.register(Contact)

# Register your models here.
