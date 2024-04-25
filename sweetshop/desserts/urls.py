from django.urls import path

from .views import *

app_name = 'list'

urlpatterns = [
    path('', Index.as_view(), name='index'), # виды десертов с подписями и фотографиями
    path('examples/<int:id>/', examples, name='example'),
    path('filling/', filling, name='filling')
    # path('create/', CreateWish.as_view(), name='create'),
    # path('edit/<int:wish_pk>/', UpdateWish.as_view(), name='edit_wish'),
    # path('delete/<int:wish_pk>/', DeleteWish.as_view(), name='delete_wish'),
    # path('details/<int:pk>/', DetailWish.as_view(), name='details_wish')
]
