from django.urls import path
from .views import login_user, register, logout_user, user_account_main, user_edit_profile

urlpatterns = [
    path('login', login_user),
    path('register', register),
    path('logout', logout_user),
    path('user', user_account_main),
    path('user/edit-profile', user_edit_profile),
]
