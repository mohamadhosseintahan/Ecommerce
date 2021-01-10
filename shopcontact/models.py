from django.db import models


# Create your models here.
class ContactUs(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='نام کامل')
    email = models.EmailField(max_length=100, verbose_name='ایمیل')
    subject = models.CharField(max_length=100, verbose_name='عنوان پیام')
    text = models.TextField(verbose_name='متن پیام')
    is_read = models.BooleanField(default=False , verbose_name='دیده شده/نشده')

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'تماس کاربران'

