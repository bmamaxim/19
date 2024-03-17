from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from catalog.models import Categories, Products


class ProductsListView(ListView):
    """
    Класс контроллер приложения каталог
    шаблон продукты
    """
    model = Products
    template_name = 'catalog/products.html'

class ProductDetailView(DetailView):
    """
    Класс контроллер приложения каталог
    шаблон продукта
    """
    model = Products
    template_name = 'catalog/product.html'

def home(request):
    """
    Функция контроллер шаблона
    домашней страницы приложения каталог
    :param request: data
    :return: dict
    """
    category = Categories.objects.all()
    context = {
        'object_list': category,
        'title': 'Главная'
    }
    return render(request, 'catalog/home.html', context)

def contacts(request):
    """
    Функция контроллер шаблона
    страницы контакты приложения каталог
    :param request: data
    :return: dict
    """
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'You have new message from {name}({email}): {message}')

    context = {
        'title': 'Обратная связь'
    }
    return render(request, 'catalog/contacts.html', context=context)

