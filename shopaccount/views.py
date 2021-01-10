from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from shopaccount.forms import LoginForm, RegisterForm, EditUserForm
from django.contrib.auth import login, get_user_model, authenticate, logout


# Create your views here.


def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')

    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        user_name = login_form.cleaned_data.get(('user_name'))
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            login_form.add_error('user_name', 'کاربری با مشخصات فوق یافت نشد')
    context = {
        'login_form': login_form
    }
    return render(request, 'account/login.html', context)


def register(request):
    register_form = RegisterForm(request.POST or None)
    if request.user.is_authenticated:
        return redirect('/')

    if register_form.is_valid():
        user_name = register_form.cleaned_data.get('user_name')
        password = register_form.cleaned_data.get('password')
        email = register_form.cleaned_data.get('email')

        User.objects.create_user(username=user_name, email=email, password=password)
        return redirect('/login')
    # print(register_form)

    context = {
        'register_form': register_form
    }
    return render(request, 'account/register.html', context)


def logout_user(request):
    logout(request)
    return redirect('/login')


@login_required(login_url='/login')
def user_account_main(request):
    return render(request, 'account/user_account_main.html', {})


@login_required(login_url='/login')
def user_edit_profile(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    edit_form = EditUserForm(request.POST or None,
                             initial={'first_name': user.first_name, 'last_name': user.last_name})
    if edit_form.is_valid():
        first_name = edit_form.cleaned_data.get('first_name')
        last_name = edit_form.cleaned_data.get('last_name')
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        edit_form = EditUserForm()

    context = {
        'edit_form': edit_form
    }
    return render(request, 'account/user_edit_profile.html', context)


def user_sidebar(request):
    return render(request, 'account/user_sidebar.html', {})
