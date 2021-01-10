from django.db.models import Q
from django.db import models
from shopcategory.models import ProductCategory


# Create your models here.


class ProductManager(models.Manager):

    def get_active_product(self):
        return self.get_queryset().filter(active=True)

    def get_by_category(self, category_name):
        return self.get_queryset().filter(categories__name__iexact=category_name, active=True)

    def get_by_id(self, product_id):
        qs = self.get_queryset().filter(pk=product_id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None

    def search(self, query):
        lookup = (Q(title__icontains=query) |
                  Q(description__icontains=query) |
                  Q(tag__title__icontains=query)
                  )

        return self.get_queryset().filter(lookup, active=True).distinct()


class Products(models.Model):
    title = models.CharField(max_length=60, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    price = models.IntegerField(verbose_name='قیمت')
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name='تصویر')
    active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')
    categories = models.ManyToManyField(ProductCategory, blank=True, verbose_name='دسته بندی')
    visit_count = models.IntegerField(default=0 , verbose_name='تعداد بازدید')

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'


    def __str__(self):
        return self.title

    objects = ProductManager()

    def get_absolute_url(self):
        return f"/products/{self.pk}/{self.title.replace(' ', '-')}"


class Gallery(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    image = models.ImageField(upload_to='products/gallery', verbose_name='تصویر')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='محصول')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تصویر'
        verbose_name_plural = 'تصاویر'
