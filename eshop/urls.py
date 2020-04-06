"""eshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from items.models import Category

from items.views import kontakt
from items.views import category
from items.views import home
from items.views import product
from kosik.views import update_cart
from kosik.views import kosik_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('cart/', kosik_view, name='kosik'),
    path('cart/<slug:url>/<int:qty>/', update_cart, name ='update_cart'),
    path('category/', include('items.urls')),
    path('kontakt/', kontakt, name='kontakt' ),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
