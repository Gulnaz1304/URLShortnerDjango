from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from shortener.models import ShortenedURL


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'shortener/home.html', {})

    def post(self, request, *args, **kwargs):
        print(request.POST['url'])
        print(request.POST.get('url'))
        return render(request, 'shortener/home.html', {})



def shortened_redirect_view(request, shortcode=None, *args, **kwargs):  # function based view

    obj = get_object_or_404(ShortenedURL, shortcode=shortcode)
    return HttpResponseRedirect(obj.url)
# Create your views here.


class ShortenedCBView(View):   # class based view
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(ShortenedURL, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)

