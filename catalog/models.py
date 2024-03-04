from django.db import models

from django.db import models

# Create your models here.
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

    def __str__(self):
        return (
            f'{self.product_name}'
            f'{self.product_price}'
            f'{self.product_category}'
        )

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
