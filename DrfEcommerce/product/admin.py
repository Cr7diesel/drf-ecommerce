from django.contrib import admin

from .models import Category, Brand, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('id', 'name')


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('id', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'is_digital', 'category', 'brand')
    list_filter = ('id', 'name', 'is_digital', 'category', 'brand')
