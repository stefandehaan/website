from django.http import HttpResponse
from django.template import loader
from .models import Album, Song


def index(request):
    all_albums = Album.objects.all()
    template = loader.get_template('')
    return HttpResponse(html)


def detail(request, album_id):
    return HttpResponse("<h2> hey " + str(album_id) + "</h2>")
