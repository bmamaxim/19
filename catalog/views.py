from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductsForm, VersionForm, ModeratorFormProducts
from catalog.models import Categories, Products, Version


class SellerViewMixin:
    pass


class ProductsCreateView(CreateView):
    """
    класс контроллер приложения каталог
    шаблон форма добавить продукт
    """
    model = Products
    form_class = ProductsForm
    success_url = reverse_lazy('catalog:list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.seller = self.request.user
        self.object.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Products, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST)
        else:
            context_data['formset'] = VersionFormset()
        return context_data


class ProductsListView(LoginRequiredMixin, ListView):
    """
    Класс контроллер приложения каталог
    шаблон продукты
    """
    model = Products
    template_name = 'catalog/products_list.html'
    login_url = 'users:login'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(publication_sign=True)
        return queryset


class ProductsDetailView(DetailView):
    """
    Класс контроллер приложения каталог
    шаблон продукта
    """
    model = Products
    template_name = 'catalog/products_detail.html'

    def get_object(self, queryset=None):
        self.object = super().get_object()
        self.object.number_of_views += 1
        self.object.save()
        return self.object


class ProductsUpdateView(UserPassesTestMixin, UpdateView):
    """
    класс контроллер приложения каталог
    шаблон форма изменить продукт
    """
    model = Products
    form_class = ProductsForm

    def test_func(self):
        if self.request.user.has_perms(
                ('catalog.change_products',)
        ) or (self.get_object().seller == self.request.user):
            return True
        return self.handle_no_permission()

    def get_form_class(self):
        if self.request.user.groups.filter(name='moderator'):
            return ModeratorFormProducts
        return ProductsForm

    def get_success_url(self):
        return reverse('products:detail', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        if not self.request.user.groups.filter(name='moderator'):
            VersionFormset = inlineformset_factory(Products, Version, form=VersionForm, extra=1)
            if self.request.method == 'POST':
                context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
            else:
                context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductsDeleteView(DeleteView):
    """
    класс контроллер приложения каталог
    шаблон форма удалить продукт
    """
    model = Products
    success_url = reverse_lazy('catalog:list')


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
