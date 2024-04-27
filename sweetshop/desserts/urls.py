from django.urls import path

from .views import *

app_name = 'list'

urlpatterns = [
    path('', Index.as_view(), name='index'), # виды десертов с подписями и фотографиями
    path('examples/<int:id>/', examples, name='example'),
    path('filling/', filling, name='filling'),
    path('filling_type/<int:id>/', filling_type, name='filling_type'),
    path('filling_detail/<int:id>/', filling_detail, name='filling_detail')
    # path('create/', CreateWish.as_view(), name='create'),
    # path('edit/<int:wish_pk>/', UpdateWish.as_view(), name='edit_wish'),
    # path('delete/<int:wish_pk>/', DeleteWish.as_view(), name='delete_wish'),
    # path('details/<int:pk>/', DetailWish.as_view(), name='details_wish')
]
