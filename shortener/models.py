from django.db import models
import random
import string


def code_generator(size=6, chars=string.ascii_lowercase + string.digits):
    new_code = ''
    for i in range(size):
        new_code += random.choice(chars)
    return new_code


class ShortenedURL(models.Model):
    url = models.CharField(max_length=200, )
    shortcode = models.CharField(max_length=15, unique=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.shortcode = code_generator()
        super(ShortenedURL, self).save(*args, **kwargs)


    def __str__(self):
        return str(self.url)
