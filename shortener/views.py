from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from shortener.models import ShortenedURL


def shortened_redirect_view(request, shortcode=None, *args, **kwargs):  # function based view

    obj = get_object_or_404(ShortenedURL, shortcode=shortcode)
    return HttpResponseRedirect(obj.url)
# Create your views here.


class ShortenedCBView(View):   # class based view
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(ShortenedURL, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)

    def post(self, request, *args, **kwargs):
        return HttpResponse