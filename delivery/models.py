from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва категорії")

    def __str__(self):
        return self.name


class Dish(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категорія")
    name = models.CharField(max_length=100, verbose_name="Назва страви")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    image = models.ImageField(upload_to='dishes/', blank=True, null=True, verbose_name="Фото")
    # Додаємо це поле, щоб виправити помилку NOT NULL
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата додавання", null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Клієнт")
    items_text = models.TextField(verbose_name="Список страв")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сума")
    address = models.CharField(max_length=255, verbose_name="Адреса доставки", default="")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата замовлення")

    def __str__(self):
        return f"Замовлення #{self.id} від {self.user.username}"