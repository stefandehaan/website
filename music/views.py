from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1> this is the music app homepage</h1>")


def detail(request, album_id):
    return HttpResponse("<h2> hey " + str(album_id) + "</h2>")