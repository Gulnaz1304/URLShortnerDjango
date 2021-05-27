from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from shortener.models import ShortenedURL
from analytics.models import ClickEvent
from .forms import SubmitUrlForm



class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form = SubmitUrlForm()
        context = {
            "title": "URLShortener",
            "form": the_form
        }
        return render(request, 'shortener/home.html', context)

    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        context = {
            "title": "URLShortener",
            "form": form
        }
        template = 'shortener/home.html'
        if form.is_valid():
            new_url = form.cleaned_data.get("url")
            obj, created = ShortenedURL.objects.get_or_create(url=new_url)
            context = {
                "object" : obj,
                "created": created

            }
            if created:
                template = 'shortener/success.html'
            else:
                template = "shortener/already-exists.html"

        return render(request, template, context)


def shortened_redirect_view(request, shortcode=None, *args, **kwargs):  # function based view

    obj = get_object_or_404(ShortenedURL, shortcode=shortcode)
    return HttpResponseRedirect(obj.url)
# Create your views here.


class URLRedirectView(View):   # class based view
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(ShortenedURL, shortcode=shortcode)
        print(ClickEvent.objects.create_event(obj))
        return HttpResponseRedirect(obj.url)

