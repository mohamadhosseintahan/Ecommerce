from django import forms
from django.contrib.auth.models import User
from django.core import validators


class EditUserForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'نام  خود را وارد کنید',
            'class': 'form-control'
        }),
        label='نام'
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'نام خانوادگی خود را وارد کنید',
            'class': 'form-control'
        }),
        label='نام خانوادگی'
    )


class LoginForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'نام کاربری خود را وارد کنید',
            'class': 'form-control'
        }),
        label='نام کاربری'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'کلمه عبور را وارد نمایید'
        }),
        label='کلمه عبور'
    )


class RegisterForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'نام کاربری خود را وارد کنید',
            'class': 'form-control'
        }),
        label='نام کاربری',
        validators=[
            validators.MaxLengthValidator(25, 'نام کاربری نباید بیشتر از 25 کارکتر باشد'),
            validators.MinLengthValidator(4, 'نام کاربری نباید کمتر از 4 کارکتر باشد')
        ]
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'ایمیل خود را وارد کنید',
            'class': 'form-control'
        }),
        label='ایمیل',
        validators=[
            validators.EmailValidator('ایمیل معتبر وارد کنید')
        ]
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'کلمه عبور را وارد نمایید'
        }),
        label='کلمه عبور',

    )
    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'تکرار کلمه عبور را وارد نمایید'
        }),
        label='تکرار کلمه عبور'
    )

    # check email validation

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # is exists checking
        is_exists_by_email = User.objects.filter(email=email).exists()

        if is_exists_by_email:
            raise forms.ValidationError('این ایمیل قبلا ثبت شده است')
        return email

    # check re_password validation
    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')

        if password != re_password:
            raise forms.ValidationError('پسورد ها میزان نیستند')
        return re_password

    # check username validation
    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        # is exists checking
        is_exists_by_username = User.objects.filter(username=user_name).exists()

        if is_exists_by_username:
            raise forms.ValidationError('قبلا کاربری با این نام کاربری ثبت نام کرده است!')
        # valid some sign
        signs = [' ', ',', '.', '!', '!', '@', '#']
        for sign in signs:
            if sign in user_name:
                raise forms.ValidationError('داخل نام کاربری از فاصله و علاِیم استفاده نکنید')
        return user_name

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError('پسورد نباید از 8 حرف کمتر باشد')
        return password
