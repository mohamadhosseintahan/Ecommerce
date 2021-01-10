from django.db import models
from django.db.models.signals import pre_save

from shopproducts.models import Products
from .utils import unique_slug_generator


# Create your models here.

class Tag(models.Model):
    title = models.CharField(max_length=30, verbose_name='عنوان')
    slug = models.SlugField(blank=True, unique=True, verbose_name='عنوان در url')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')
    active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')
    products = models.ManyToManyField(Products, verbose_name='محصولات')

    class Meta:
        verbose_name = 'برچسب'
        verbose_name_plural = 'برچسب ها'

    def __str__(self):
        return self.title


def tag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(tag_pre_save_receiver, sender=Tag)
