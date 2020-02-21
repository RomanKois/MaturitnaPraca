from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from items.models import Category, Product
from django.db.models import Q


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

def hladaj(request):
    querry = request.GET.get('q')
    categories = Category.objects.all()
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




    
