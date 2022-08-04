from django.urls import path
from . import views
urlpatterns = [
    path('dashboard/', views.home, name='dashboard-home'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('products/', views.product, name='dashboard-products'),
    path('product/update/<int:pk>/', views.product_update,
         name='dashboard-product-update'),
    path('product/delete/<int:pk>/', views.product_delete,
         name='dashboard-product-delete'),
    path('orders/', views.orders, name='dashboard-orders'),
]
