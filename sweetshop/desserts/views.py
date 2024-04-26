from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Decorations, Fillings, ExampleDecoration, ExampleFilling


class Index(ListView):
    model = Decorations
    template_name = 'desserts/index.html'


def examples(request, id):
    objects = Decorations.objects.get(id=id)
    return render(request, 'desserts/examples.html', {'objects': objects})


def filling(request):
    objects = Fillings.objects.all()
    return render(request, 'desserts/filling.html', {'objects': objects})


def filling_detail(request, id):
    objects = ExampleFilling.objects.get(id=id)
    return render(request, 'desserts/filling_detail.html', {'objects': objects})

