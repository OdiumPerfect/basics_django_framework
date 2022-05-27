from django.shortcuts import render


def index(request):

    content = {
        'title':'Geekshop'
    }

    return render(request,'mainapp/index.html', content)


def products(request):


    categories = [
        {'name': 'Новинки'},
        {'name': 'Одежда'},
        {'name': 'Обувь'},
        {'name': 'Аксессуары'},
        {'name': 'Подарки'}
    ]

    content = {
        'title':'Geekshop | Каталог',
        'categories': categories
    }


    return render(request,'mainapp/products.html', content)