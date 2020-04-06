from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from items.models import Category, Product
from django.db.models import Q
import operator
import random

def home(request):
    context = {}
    categories = Category.objects.all().order_by("name")
    products = Product.objects.all().filter(available = True)
    context['category'] = categories
    random_product= random.sample(list(products), 5)
    context['random'] = random_product
    context['products'] = products
    context['itemCount'] = getItemCount(request)
    return render(request, 'items/MainPage.html', context)



def category(request, category):    
    cat = Category.objects.get(url=category)
    categories = Category.objects.all()
    products_ordered = Product.objects.filter(category=cat, available = True).order_by("name")
    context = {}
    context['category'] = categories
    context['products'] = products_ordered
    context['itemCount'] = getItemCount(request)
    return render(request, 'items/Category.html', context)

def product(request, category, product):
    categories = Category.objects.all().order_by("name")
    product = Product.objects.get(url=product)
    context = {}
    context['category'] = categories
    context['product'] = product
    context['itemCount'] = getItemCount(request)
    return render(request, 'items/Product.html', context)



def kontakt(request):
    context = {}
    categories = Category.objects.all().order_by("name")
    context['category'] = categories
    context['itemCount'] = getItemCount(request)
    return render(request, 'items/kontakt.html', context)

def hladaj(request):
    querry = request.GET.get('q')
    categories = Category.objects.all().order_by("name")
    context = {
        "category": categories
    }

    if len(querry) != 0:
        queryset = getQuery(querry)
        if len(queryset) != 0:
            context['products'] = queryset
        else:
            context['nores'] = "Produkt: " + str(querry) + " nenájdený"
            context['products'] = []
    else:
        context['nores'] = "Prázdne hľadanie"
        context['products'] = []

    context['itemCount'] = getItemCount(request)
    return render(request, 'items/search.html', context)


def getQuery(keyword):
    queryset = None
    queries = keyword.split(" ")
    for q in queries:
        products = Product.objects.filter(
            Q(name__icontains=q)
        ).distinct()

        queryset = [p for p in products]

    return list(set(queryset))


# Toto nie je veiw FYI the request parameter is just a coinsidence
def getItemCount(request):
    count = None
    try:
        count = len(request.session['kosik'])
    except KeyError:
        count = 0

    return count
