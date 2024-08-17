from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home/home.html')


def product_list(request):
    return render(request, 'home/listProduct.html')


def product(request):
    return render(request, 'home/product.html')


def vendor(request):
    return render(request, 'home/vendor.html')
