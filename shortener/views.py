from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


def shortened_redirect_view(request, *args, **kwargs):  # function based view
    return HttpResponse("hello")
# Create your views here.


class ShortenedCBView(View):   # class based view
    def get(self, request, *args, **kwargs):
        return HttpResponse('hello')
