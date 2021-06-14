from django.db import models
from .utils import code_generator, create_shortcode
from django.conf import settings
from .validators import validate_url, validate_dot_com
# from django.urls import reverse
from django_hosts.resolvers import reverse


SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)


class ShortenedURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(ShortenedURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs


class ShortenedURL(models.Model):
    url = models.CharField(max_length=200, validators=[validate_url, validate_dot_com])
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    objects = ShortenedURLManager()

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = hex(hash(self.id))[2:]

        if not "http" in self.url:
            self.url = "http//" + self.url
        super(ShortenedURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def get_short_url(self):
        url_path = reverse('scode', kwargs={'shortcode': self.shortcode}, host='www', scheme="http", port='8000')
        return url_path
