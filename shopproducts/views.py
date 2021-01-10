import itertools

from django.shortcuts import render
from django.views.generic import ListView, DetailView

from shopcategory.models import ProductCategory
from shoporder.forms import UserNewOrderForm
from shoptags.models import Tag
from .models import Products, Gallery
from django.http import Http404


# Create your views here.

class ProductsList(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 6

    # def get_queryset(self):
    #     return Products.objects.get_queryset().filter(active=True)
    queryset = Products.objects.get_active_product()


# class ProductsDetail(DetailView):
#     template_name = 'products/products_detail.html'
#     queryset = Products.objects.all()

class ProductListByCategory(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 6

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        category = ProductCategory.objects.filter(name__iexact=category_name).first()
        if category is None:
            raise Http404('صفحه مورد نظر یافت نشد')
        return Products.objects.get_by_category(category_name)


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def product_detail(request, *args, **kwargs):
    # getting product for detail
    product_id = kwargs['productId']
    new_order_form = UserNewOrderForm(request.POST or None, initial={'product_id': product_id})
    product : Products = Products.objects.get_by_id(product_id)

    product.visit_count += 1
    product.save()
    # galleries picture
    galleries = Gallery.objects.filter(product_id=product_id)
    grouped_galleries = list(my_grouper(3, galleries))

    # related products
    related_products = Products.objects.filter(categories__products=product).distinct()
    grouped_related_products = list(my_grouper(3, related_products))

    context = {
        'product': product,
        'grouped_galleries': grouped_galleries,
        'grouped_related_products': grouped_related_products,
        'new_order_form': new_order_form
    }
    #
    # tags = Tag.objects.filter(title__icontains='django').first()
    # print(tags.products.all())

    if product is None or not product.active:
        raise Http404
    else:
        return render(request, 'products/products_detail.html', context)


class SearchProductView(ListView):
    template_name = 'products/products_list.html'

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            return Products.objects.search(query)
        return Products.objects.get_active_product()

    paginate_by = 6


def products_categories_partial(request):
    categories = ProductCategory.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'products/products_categories_partial.html', context)
