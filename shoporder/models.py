from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from shopproducts.models import Products


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    is_paid = models.BooleanField(verbose_name='پرداخت شده / نشده')
    payment_date = models.DateTimeField(verbose_name='تاریخ پرداخت', null=True, blank=True)

    def __str__(self):
        return self.owner.get_full_name()

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد های خرید'


class OrderDetail(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='محصول')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سبد خرید')
    price = models.IntegerField(verbose_name='قیمت')
    count = models.IntegerField(verbose_name='تعداد')

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = 'جزییات سبد خرید'
        verbose_name_plural = 'جزییات سبد های خرید'

    def finall_price(self):
        return self.price * self.count