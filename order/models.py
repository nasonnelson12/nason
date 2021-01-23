from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
from django.conf import settings
from django.db.models import Sum
from django.db.models import Count

from shop.models import Product, Variation


# Create your models here.


class ShopCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)
    color = models.CharField(max_length=50, blank=True, null=True)
    size = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return self.product.title

    def price(self):
        return self.product.price

    def get_total_product_price(self):
        return self.quantity * self.product.price

    def get_total_discount_product_price(self):
        return self.quantity * self.product.discount_price

    def get_amount_saved(self):
        return self.get_total_product_price() - self.get_total_discount_product_price()

    def get_final_price(self):
        if self.product.discount_price:
            return self.get_total_discount_product_price()
        return self.get_total_product_price()

class ShopCartForm(ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity', 'color', 'size']

class Order(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Preaparing', 'Preaparing'),
        ('OnShipping', 'OnShipping'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    )
    region = (
        ('Mwanza', 'Mwanza'),
    )
    district = (
        ('Ilemela', 'Ilemela'),
        ('Nyamagana', 'Nyamagana'),
        ('Misungwi', 'Misungwi'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    code = models.CharField(max_length=5, editable=False)
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    phone = models.CharField(max_length=20)
    region = models.CharField(max_length=100, choices=region, default='Mwanza')
    district = models.CharField(max_length=100, choices=district, default='Nyamagana')
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    total = models.FloatField()
    status = models.CharField(max_length=15, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=20)
    adminnote = models.CharField(blank=True, max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone', 'region', 'district', 'street_address', 'apartment_address']

class DeliveredPayment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class OrderProduct(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Canceled', 'Canceled'),
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    color = models.CharField(max_length=50, blank=True, null=True)
    size = models.CharField(max_length=60, blank=True, null=True)
    price = models.FloatField()
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.title





