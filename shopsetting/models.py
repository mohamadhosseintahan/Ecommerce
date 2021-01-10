from django.db import models


# Create your models here.

class SiteSetting(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان')
    address = models.CharField(max_length=50, verbose_name='آدرس')
    phone = models.CharField(max_length=50, verbose_name='تلفن')
    mobile = models.CharField(max_length=50, verbose_name='موبایل')
    fax = models.CharField(max_length=50, verbose_name='فکس')
    email = models.EmailField(max_length=50, verbose_name='ایمیل')
    about_us = models.TextField(max_length=100, verbose_name='درباره ما')
    copy_right = models.CharField(max_length=100, verbose_name='کپی رایت')

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات سایت'

    def __str__(self):
        return self.title
