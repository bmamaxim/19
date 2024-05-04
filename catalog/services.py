from django.core.cache import cache

from catalog.models import Categories
from config.settings import CACHE_ENABLED


def get_category_from_cache():
    """
    Функция кеширования категорий продуктов
    если кеша нет возвращает данные из БД
    """
    if not CACHE_ENABLED:
        return Categories.objects.all()
    key = 'category_list'
    category = cache.get(key)
    if category is not None:
        return category
    category = Categories.objects.all()
    cache.set(key, category)
    return category
