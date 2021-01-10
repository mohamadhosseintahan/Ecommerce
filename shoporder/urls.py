from django.urls import path

from shoporder.views import add_new_order, user_open_order , remove_order

urlpatterns = [
    path('order', add_new_order),
    path('open-order', user_open_order),
    path('remove-order/<detail_id>', remove_order),
]
