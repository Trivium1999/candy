from django.shortcuts import render
from .models import Decorations, Fillings, ExampleDecoration, ExampleFilling


def index(request):
    example = ExampleDecoration.objects.all()
    decor = Decorations.objects.all()
    context = {'decor': decor, 'example': example}
    return render(request, 'desserts/index.html', context)


def tags(request):
#     # tags = Tag.objects.all()
    context = {'tags': tags}
    return render(request, 'desserts/tags.html', context)


def examples(request, id):
    examples = Decorations.objects.get(id=id)
    context = {'examples': examples}
    return render(request, 'desserts/examples.html', context)


def filling(request):
    fillings = Fillings.objects.all()
    context = {'fillings': fillings}
    return render(request, 'desserts/filling.html', context)
