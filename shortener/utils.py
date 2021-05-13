import random
import string


def code_generator(size=6, chars=string.ascii_lowercase + string.digits):
    new_code = ""
    for i in range(size):
        new_code += random.choice(chars)
    return new_code


def create_shortcode(instance, size=6):
    new_code = code_generator(size=size)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(shortcode=new_code).exists()
    if qs_exists:
        return create_shortcode(instance, size=size)
    return new_code

