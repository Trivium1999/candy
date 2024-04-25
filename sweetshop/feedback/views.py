from django.shortcuts import render
from .models import Reviews


def about(request):
    context = {'title': 'Обо мне', 'heading': 'Обо мне'}
    return render(request, 'feedback/about.html', context)


def contact(request):
    context = {'title': 'Контакты', 'heading': 'Контакты'}
    return render(request, 'feedback/contact.html', context)


def reviews(request):
    reviews = Reviews.objects.all()
    context = {'title': 'Отзывы', 'heading': 'Отзывы', 'reviews': reviews}
    return render(request, 'feedback/reviews.html', context)
