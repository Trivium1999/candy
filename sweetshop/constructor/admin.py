from django.contrib import admin

from .models import (
                     Cake,
                     CakeFilling,
                     CakeDecoration,
                     Cupcake,
                     CupcakeFilling,
                     CupcakeDecoration,
                     OtherDessert,
                     BentoCake,
                     BentoFilling
                     )


@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'date', 'description', 'filling', 'decoration', 'price')
    empty_value_display = '-пусто-'


@admin.register(CakeFilling)
class CakeFillingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'description', 'price')
    empty_value_display = '-пусто-'


@admin.register(CakeDecoration)
class CakeDecorationAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description', 'price')
    empty_value_display = '-пусто-'


@admin.register(Cupcake)
class CupcakeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'date', 'description', 'filling', 'decoration', 'price')
    empty_value_display = '-пусто-'


@admin.register(CupcakeFilling)
class CupcakeFillingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'description')
    empty_value_display = '-пусто-'


@admin.register(CupcakeDecoration)
class CupcakeDecorationAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description', 'price')
    empty_value_display = '-пусто-'


@admin.register(OtherDessert)
class OtherDessertAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description', 'price')
    empty_value_display = '-пусто-'


@admin.register(BentoCake)
class BentoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'date', 'description', 'filling', 'price')
    empty_value_display = '-пусто-'


@admin.register(BentoFilling)
class BentoFillingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'description')
    empty_value_display = '-пусто-'
