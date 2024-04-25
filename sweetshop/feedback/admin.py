from django.contrib import admin

from .models import Reviews


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'description')
    empty_value_display = '-пусто-'
