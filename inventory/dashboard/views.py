from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm
# Create your views here.


@login_required
def home(request):
    return render(request, 'dashboard/home.html')


@login_required
def staff(request):
    return render(request, 'dashboard/staff.html')


@login_required()
def product(request):
    items = Product.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-products')
    else:
        form = ProductForm()
    context = {'items': items,
               'form': form
               }
    return render(request, 'dashboard/product.html', context)


@login_required()
def orders(request):
    return render(request, 'dashboard/orders.html')
