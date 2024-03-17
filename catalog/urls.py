from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contacts, ProductsListView, ProductDetailView

app_name = 'products'

urlpatterns = [
    path('', home),
    path('contacts/', contacts, name='contacts'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('<int:pk>', ProductDetailView.as_view(), name='product'),
]
