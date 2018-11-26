from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    # Home page /music/
    url(r'^$', views.IndexView.as_view(), name="index"),

    # Album detail /music/:id/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),

    # API for favourite a song /music/:id/favourite/
    url('album/add/$', views.AlbumCreate.as_view(), name="album-add")
]
