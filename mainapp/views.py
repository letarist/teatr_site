from datetime import datetime

from django.conf import settings
from django.shortcuts import render
from django.views.generic import DetailView
from mainapp.models import Artist, Genre, Repertoire


def main(request):
    artists = Artist.objects.all()
    links = Genre.objects.all()
    context = {'title': 'ГлАвНаЯ', 'time': datetime.now(), 'artists': artists, 'links': links,
               'media_url': settings.MEDIA_URL}
    return render(request, 'mainapp/index.html', context)


def contacts(request):
    context = {'title': 'КоНтАкТы', 'time': datetime.now()}
    return render(request, 'mainapp/contacts.html', context)


def genre(request, pk=None):
    title = Genre.objects.filter(pk=pk).first()
    links = Genre.objects.all()
    work = Repertoire.objects.filter(genre=pk)
    context = {'links': links, 'work': work, 'time': datetime.now(), 'title': title, 'media_url': settings.MEDIA_URL}
    return render(request, 'mainapp/works.html', context)


class PostDetail(DetailView):
    model = Repertoire
    template_name = 'mainapp/repertoire.html'

