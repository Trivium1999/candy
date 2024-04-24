from django.contrib import admin

from .models import Decorations, Fillings, ExampleDecoration, ExampleFilling


@admin.register(ExampleDecoration)
class ExampleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')
    empty_value_display = '-пусто-'


@admin.register(Decorations)
class TagAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')
    empty_value_display = '-пусто-'


@admin.register(ExampleFilling)
class TagAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')
    empty_value_display = '-пусто-'


@admin.register(Fillings)
class FillingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description')
    empty_value_display = '-пусто-'
