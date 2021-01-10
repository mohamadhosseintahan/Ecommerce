import itertools

from django.shortcuts import render, redirect

from shopproducts.models import Products
from shopslider.models import Slider
from shopsetting.models import SiteSetting

from shopcategory.models import ProductCategory


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def home_page(request):
    sliders = Slider.objects.all()
    most_visit_products = Products.objects.order_by('-visit_count').all()[:8]
    latest_products = Products.objects.order_by('-id').all()[:8]
    context = {
        'data': 'new data',
        'sliders': sliders,
        'most_visit_products': my_grouper(4, most_visit_products),
        'latest_products': my_grouper(4, latest_products),
    }
    return render(request, 'home_page.html', context)


def header(request):
    context = {
        'title': 'this is title'
    }
    return render(request, 'shared/Header.html', context)


def footer(request):
    setting = SiteSetting.objects.first()
    context = {
        'setting': setting
    }
    return render(request, 'shared/Footer.html', context)
