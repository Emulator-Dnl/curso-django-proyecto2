from django import template
# hacemos referencia no al directorio actual '.' sino a pages porque está por fuera
from pages.models import Page

register = template.Library()

@register.simple_tag
def get_page_list():
    pages = Page.objects.all()
    return pages