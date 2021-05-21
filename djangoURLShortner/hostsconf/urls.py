from django.contrib import admin
from django.urls import path
from shortener.views import shortened_redirect_view, ShortenedCBView
from .views import wildcard_redirect


urlpatterns = [
    path(r'^(?P<path>.*', wildcard_redirect),

]
