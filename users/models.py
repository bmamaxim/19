from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
    avatar = models.ImageField(upload_to='image/', verbose_name='изображение', **NULLABLE)
    phone = models.CharField(max_length=200, verbose_name='телефон', unique=True)
    country = models.CharField(max_length=200, verbose_name='страна')
    username = None

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'продавец'
        verbose_name_plural = 'продавцы'

    def __str__(self):
        return f"{self.username} {self.phone} {self.country}"
