from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Product
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

    context = {'items': items}
    return render(request, 'dashboard/product.html', context)

@login_required()
def orders(request):
    return render(request, 'dashboard/orders.html')
