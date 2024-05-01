from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import contacts, ProductsListView, ProductsDetailView, ProductsCreateView, ProductsUpdateView, \
    ProductsDeleteView, CategoriesListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', CategoriesListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('create/', ProductsCreateView.as_view(), name='create'),
    path('view/', ProductsListView.as_view(), name='list'),
    path('view/<int:pk>', cache_page(120)(ProductsDetailView.as_view()), name='detail'),
    path('update/<int:pk>', ProductsUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ProductsDeleteView.as_view(), name='delete')
]
