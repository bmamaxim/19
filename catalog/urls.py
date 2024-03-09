from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contacts, products, product

app_name = 'products'

urlpatterns = [
    path('', home),
    path('contacts/', contacts, name='contacts'),
    path('products/', products, name='products'),
    path('<int:pk>', product, name='product'),
]
