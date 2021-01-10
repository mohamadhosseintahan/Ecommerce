from django.db import models


# Create your models here.
class Slider(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    link = models.URLField(max_length=100, verbose_name='آدرس')
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to='sliders/', blank=True, null=True, verbose_name='تصویر')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدر ها'
