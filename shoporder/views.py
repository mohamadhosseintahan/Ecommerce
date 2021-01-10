from itertools import product

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from shopproducts.models import Products
from .forms import UserNewOrderForm
from .models import Order,OrderDetail

@login_required(login_url='/login')
def add_new_order(request):
    new_order_form = UserNewOrderForm(request.POST or None)
    if new_order_form.is_valid():
        order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
        if order is None:
            order = Order.objects.create(owner_id=request.user.id, is_paid=False)
        product_id = new_order_form.cleaned_data.get('product_id')
        count = new_order_form.cleaned_data.get('count')
        if count < 1:
            count = 1
        product = Products.objects.get_by_id(product_id=product_id)

        order.orderdetail_set.create(product_id=product.id, price=product.price, count=count)
        return redirect(f"products/{product.pk}/{product.title.replace(' ' , '-')}")
    return redirect('/')

@login_required(login_url='/login')
def user_open_order(request):
    context={
        'order' : None,
        'order_detail' : None
    }
    order = Order.objects.filter(owner_id=request.user.id , is_paid=False).first()
    if order is not None:
        context['order'] = order
        context['order_detail'] = order.orderdetail_set.all()

    return render(request , 'order/order_page.html' , context)

@login_required(login_url='/login')
def remove_order(request , *args ,**kwargs):
    detail_id = kwargs.get('detail_id')
    if detail_id is not None:
        order_detail = OrderDetail.objects.get_queryset().get(id=detail_id)
        if order_detail is not None:
            order_detail.delete()
            return redirect('/open-order')
    return redirect('/')
