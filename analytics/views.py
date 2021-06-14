from django.shortcuts import render
from .models import ClickEvent
from shortener.models import ShortenedURL


def all_links(request):
    objects = ClickEvent.objects.all()


    context = {
        'objects': objects,




    }

    return render(request, 'shortener/all-links.html', context=context)


# Create your views here.
