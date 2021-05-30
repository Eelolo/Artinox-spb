from django import template
from artinox_spb_app.models import *

register = template.Library()

@register.simple_tag()
def get_page_info():
    return Page.objects.filter(pk__gte=0)


@register.simple_tag()
def get_page_content():
    return PageContent.objects.all()
