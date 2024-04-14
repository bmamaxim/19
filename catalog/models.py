from django.db import models

from config import settings

NULLABLE = {'blank': True, 'null': True}


class Categories(models.Model):
    category_name = models.CharField(max_length=200, verbose_name='категория')
    category_description = models.CharField(max_length=200, verbose_name='описание', **NULLABLE)

    def __str__(self):
        return f'{self.category_name} {self.category_description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Products(models.Model):
    product_name = models.CharField(max_length=200, verbose_name='название')
    product_description = models.CharField(max_length=200, verbose_name='описание', **NULLABLE)
    product_image = models.ImageField(upload_to='image/', verbose_name='изображение', **NULLABLE)
    product_category = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name='категория')
    product_price = models.IntegerField(verbose_name='цена', **NULLABLE)
    created_at = models.DateField(auto_now_add=True, verbose_name='дата записи', **NULLABLE)
    updated_at = models.DateField(auto_now_add=True, verbose_name='последние изменения', **NULLABLE)

    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='продавец',
                               **NULLABLE)

    def __str__(self):
        return (
            f'{self.product_name}'
            f'{self.product_price}'
            f'{self.product_category}'
        )

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Version(models.Model):
    version_number = models.IntegerField(default=0, verbose_name='номер версии')
    version_name = models.CharField(max_length=100, verbose_name='описание', **NULLABLE)
    version_sign = models.BooleanField(default=True, verbose_name='версия')

    product_name = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='название')

    def __str__(self):
        return f'{self.version_number}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
