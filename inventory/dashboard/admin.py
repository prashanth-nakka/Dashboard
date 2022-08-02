from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Product, Order
# Register your models here.

admin.site.site_header = 'DJ-Inventory Dashboard'


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'category', 'created_at',)
    list_filter = ('category',)


admin.site.register(Product, ProductsAdmin)
admin.site.register(Order)
# admin.site.unregister(Group)
