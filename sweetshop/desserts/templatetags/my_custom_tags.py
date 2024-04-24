import desserts.views as views
from django import template
from django.utils import timezone


register = template.Library()


@register.simple_tag()
def year():
    """Добавляет переменную с текущим годом."""
    year = timezone.now().year
    return year


# @register.simple_tag()
# def get_cakes_with_berries():
#     return Tag.objects.get(id=7)
