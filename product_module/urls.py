from django.urls import path

from .views import search, cart, removecart

urlpatterns = [
    path('', search),
    path('cart/', cart),
    path('cart/remove/<int:id>', removecart),
]