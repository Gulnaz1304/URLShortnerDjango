import random
import string
from django.conf import settings
from django.utils.crypto import get_random_string

SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN", 6)


def code_generator(instance, size=SHORTCODE_MIN, chars=string.ascii_lowercase + string.digits):
    return get_random_string(size, chars)


def create_shortcode(instance, size=SHORTCODE_MIN):
    new_code = code_generator(instance, size)
    cls = instance.__class__
    qs_exists = cls.objects.filter(shortcode=new_code).exists()
    if qs_exists:
        return create_shortcode(instance, size=size)
    return new_code

