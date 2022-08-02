from django.urls import path
from . import views
urlpatterns = [
    path('dashboard/', views.home, name='dashboard-home'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('products/', views.product, name='dashboard-products'),
    path('orders/', views.orders, name='dashboard-orders'),
]
