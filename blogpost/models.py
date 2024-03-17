from django.db import models

NULLABLE = {'blank': True, 'null': True}
class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name='заголовок')
    slug = models.CharField(max_length=200, verbose_name='урл')
    content = models.TextField(verbose_name='содержание', **NULLABLE)
    preview = models.ImageField(upload_to='image/', verbose_name='изображение', **NULLABLE)
    created_at = models.DateField(auto_now_add=True, verbose_name='дата записи', **NULLABLE)
    publication_sign = models.BooleanField(default=True, verbose_name='публикация')
    number_of_views = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return f"{self.title} {self.slug} {self.content}"

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'

