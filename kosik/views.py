from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


def kosik(request):
    context = {}
    context['itemCount'] = getItemCount(request)
    return render(request, 'kosik/kosik.html', context)


def addToCart(request, slug):
    try:
        if not isInSession(slug, request.session['kosik']):
            request.session['kosik'].append({
                "slug": slug,
                "amount": 1
            })
            print("Bol pridany item")
        else:
            print("Item sa uz raz nachadza v session")
        print(request.session['kosik'])
    except KeyError:
        request.session['kosik'] = []
        request.session['kosik'].append({
            "slug": slug,
            "amount": 1
        })
        print(request.session['kosik'])

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def isInSession(slug, session):
    for i in session:
        if i['slug'] == slug:
            return True
    return False


def getItemCount(request):
    count = None
    try:
        count = len(request.session['kosik'])
    except KeyError:
        count = 0

    return count