import json

from django.core.management import BaseCommand
from django.db import connection

from catalog.models import Categories, Products


class Command(BaseCommand):

    def handle(self, *args, **options):

        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE catalog_categories RESTART IDENTITY CASCADE;')

        Categories.objects.all().delete()
        Products.objects.all().delete()

        with open('data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

            products_for_create = []
            categories_for_create = []

            for category in data:
                if category["model"] == "catalog.categories":
                    categories_for_create.append(Categories(category_name=category['fields']['category_name'],
                                                            category_description=category['fields']
                                                            ['category_description']))
            Categories.objects.bulk_create(categories_for_create)
            for product in data:
                if product["model"] == "catalog.products":
                    products_for_create.append(Products(product_name=product['fields']['product_name'],
                                                        product_description=product['fields']['product_description'],
                                                        product_category=Categories.objects.get(
                                                            pk=product['fields']['product_category']),
                                                        product_price=product['fields']['product_price']))

            Products.objects.bulk_create(products_for_create)
