from django.urls import path
from .views import (
    product,
    kontakt,
    category,
    hladaj,
 
)

urlpatterns = [ 
    path('search/', hladaj, name='searchResults'),
    path('<slug:category>/', category, name='category'),
    path('<slug:category>/<slug:product>/', product, name='product'),
    
]