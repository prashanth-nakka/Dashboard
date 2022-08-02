from django.db import models

# Create your models here.

CATEGORY = (
    ('Stattionary', 'stationary'),
    ('Electronics', 'electronics'),
    ('Food', 'food'),
)


class Product(models.Model):
    name = models.CharField(max_length=100 ,null=True)
    category = models.CharField(max_length=20, choices=CATEGORY, null=True)
    quantity = models.PositiveIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}, {self.quantity}'

    