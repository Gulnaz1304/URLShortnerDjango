from django.db import models
from shortener.models import ShortenedURL


class ClickEventManager(models.Manager):
    def create_event(self, instance):
        if isinstance(instance, ShortenedURL):
            obj, created = self.get_or_create(sh_url=instance)
            obj.count += 1
            obj.save()
            return obj.count
        return None


class ClickEvent(models.Model):
    sh_url = models.OneToOneField(ShortenedURL, on_delete=models.DO_NOTHING)
    count = models.IntegerField(default=0)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    objects = ClickEventManager()

    def __str__(self):
        return "{i}".format(i=self.count)
