from django.shortcuts import render

from mainapp.models import ProductCategories, Product


def index(request):
    content = {
        'title': 'Geekshop'
    }
    return render(request,'mainapp/index.html', content)


def products(request):
    content = {
        'title': 'Geekshop - Каталог',
        'categories': ProductCategories.objects.all(),
        'products': Product.objects.all()
    }
    return render(request,'mainapp/products.html', content)