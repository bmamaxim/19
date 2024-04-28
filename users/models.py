from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    avatar = models.ImageField(upload_to='image/', verbose_name='изображение', blank=True, null=True)
    phone = models.CharField(max_length=200, verbose_name='телефон', unique=True, blank=True, null=True)
    country = models.CharField(max_length=200, verbose_name='страна', blank=True, null=True)
    username = None

    email = models.EmailField(unique=True, verbose_name='элктронная почта')

    ver_code = models.CharField(max_length=4, verbose_name='код верификации', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

        permissions = (
            (
                'cancel',
                'отмена публикации'
            ),
            (
                'change description',
                'изменить описание'
            ),
            (
                'change category',
                'изменить категорию'
            ),
        )

    def __str__(self):
        return f"{self.username} {self.phone} {self.country}"
