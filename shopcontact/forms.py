from django import forms
from django.core import validators

class CreateContactForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'نام کامل خود را وارد کنید',
            'class': 'form-control'
        }),
        validators=[validators.MaxLengthValidator(100 , 'اسم نباید بیش از 100 کاراکتر داشته باشد')]
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'ایمیل خود را وارد کنید',
            'class': 'form-control'
        }),
        validators=[validators.MaxLengthValidator(100, 'ایمیل نباید بیش از 100 کاراکتر داشته باشد')]
    )
    subject = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'عنوان خود را وارد کنید',
            'class': 'form-control'
        }),
        validators=[validators.MaxLengthValidator(100, 'عنوان نباید بیش از 100 کاراکتر داشته باشد')]
    )
    text = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'متن پیام خود را وارد کنید',
            'class': 'form-control'
        })
    )

