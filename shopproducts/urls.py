from django.urls import path
from .views import (ProductsList, ProductListByCategory,
                    product_detail, SearchProductView,
                    products_categories_partial,)

urlpatterns = [
    path('products', ProductsList.as_view()),
    path('products/<productId>/<title>', product_detail),
    path('products/search', SearchProductView.as_view()),
    path('products/<category_name>', ProductListByCategory.as_view()),
    path('products_categories_partial', products_categories_partial, name='products_categories_partial'),

]
