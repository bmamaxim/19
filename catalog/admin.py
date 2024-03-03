from django.contrib import admin

from catalog.models import Categories, Products


# Register your models here.

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name',)

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'product_price', 'product_category',)
    list_filter = ('product_category',)
    search_fields = ('product_name', 'product_description',)
