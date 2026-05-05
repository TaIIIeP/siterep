from django.contrib import admin
from .models import Category, Dish, Courier


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'created_at', 'updated_at')


@admin.register(Courier)
class CourierAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'created_at', 'updated_at')


from django.contrib import admin

# Register your models here.
