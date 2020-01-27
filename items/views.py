from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from items.models import Category, Product


def home(request):
    context = {}
    categories = Category.objects.all()
    products = Product.objects.all()
    context['category'] = categories
    context['products'] = products
    return render(request, 'items/home.html', context)



def category(request, category):    
    cat = Category.objects.get(url=category)
    categories = Category.objects.all()
    products = Product.objects.filter(category=cat) 
    context = {}
    context['category'] = categories
    context['products'] = products
    return render(request, 'items/Category.html', context)

def product(request, category, product):
    categories = Category.objects.all()
    product = Product.objects.get(url=product)
    context = {}
    context['category'] = categories
    context['product'] = product
    return render(request, 'items/Product.html', context)



def kontakt(request):
    context = {}
    categories = Category.objects.all()
    context['category'] = categories
    return render(request, 'items/kontakt.html', context)




    
