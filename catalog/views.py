from django.shortcuts import render

from catalog.models import Categories, Products


# Create your views here.

def home(request):
    category = Categories.objects.all()
    context = {
        'object_list': category
    }
    return render(request, 'catalog/home.html', context)

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'You have new message from {name}({email}): {message}')
    return render(request, 'catalog/contacts.html')

def products(request):
    product = Products.objects.all
    context = {
        'object_list': product
    }
    return render(request, 'catalog/products.html', context=context)

def product(request, pk):
    context = {
        'object_list': Products.objects.get(pk=pk)
    }
    return render(request, 'catalog/product.html', context=context)
