from django.urls import path

from .views import about, contact, reviews

app_name = 'feedback'

urlpatterns = [
    path('about/', about, name='about'), # виды десертов с подписями и фотографиями
    path('contact/', contact, name='contact'),
    path('reviews/', reviews, name='reviews'),
    
    # path('wish_user/<int:author_id>/', WishesForUser.as_view(), name='all_wish'),
    # path('about/', about, name='about'),
    # path('create/', CreateWish.as_view(), name='create'),
    # path('edit/<int:wish_pk>/', UpdateWish.as_view(), name='edit_wish'),
    # path('delete/<int:wish_pk>/', DeleteWish.as_view(), name='delete_wish'),
    # path('details/<int:pk>/', DetailWish.as_view(), name='details_wish')
]
