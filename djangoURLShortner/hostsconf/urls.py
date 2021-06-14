from django.contrib import admin
from django.urls import path
from shortener.views import  URLRedirectView
from .views import wildcard_redirect


urlpatterns = [
    path(r'^(?P<path>.*', wildcard_redirect),

]
