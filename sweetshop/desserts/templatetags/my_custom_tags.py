import desserts.views as views
from django import template
from django.utils import timezone
from ..models import ExampleFilling


register = template.Library()


@register.simple_tag()
def year():
    """Добавляет переменную с текущим годом."""
    year = timezone.now().year
    return year


@register.simple_tag()
def get_all_example_filling():
    return ExampleFilling.objects.all()
