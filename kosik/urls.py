from django.urls import path
from .views import (
    kosik,
    addToCart,
)

urlpatterns = [
    path('', kosik, name='kosik'),
    path('<slug:slug>/', addToCart, name='addToCart'),
]