from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'dashboard/home.html')


def staff(request):
    return render(request, 'dashboard/staff.html')


def product(request):
    return render(request, 'dashboard/product.html')

def orders(request):
    return render(request, 'dashboard/orders.html')
