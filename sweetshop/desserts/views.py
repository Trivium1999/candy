from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import Decorations, Fillings, ExampleDecoration, ExampleFilling


class Index(TemplateView):
    template_name = 'desserts/index.html'
    extra_context = {'decor': Decorations.objects.all()}


def tags(request):
#     # tags = Tag.objects.all()
    context = {'tags': tags}
    return render(request, 'desserts/tags.html', context)


def examples(request, id):
    objects = Decorations.objects.get(id=id)
    return render(request, 'desserts/examples.html', {'objects': objects})


def filling(request):
    objects = Fillings.objects.all()
    return render(request, 'desserts/filling.html', {'objects': objects})
