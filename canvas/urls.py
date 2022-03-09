from django.urls import include,path
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.conf import settings

from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('canvas/<str:name>',views.canvas, name="canvas"),
    path('new',views.create, name="new"),
    path('update',views.update, name="update"),
    path('change',views.change, name="change"),
    path('search',views.search, name="search"),
    path(
        "favicon.ico",
        RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),
    ),
]