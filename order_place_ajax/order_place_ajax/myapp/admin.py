from django.contrib import admin
from django.db import models

from .models import Order, OrderItem, Product

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    Product.save


@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    Order.save


@admin.register(OrderItem)
class OrderitemModelAdmin(admin.ModelAdmin):
    OrderItem.save
