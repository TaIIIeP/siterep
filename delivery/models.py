from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва категорії")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено о")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Оновлено о")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"


class Dish(models.Model):
    name = models.CharField(max_length=150, verbose_name="Назва страви")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Ціна")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категорія")

    # НОВЕ ПОЛЕ ДЛЯ ФОТО:
    image = models.ImageField(upload_to='dishes/', blank=True, null=True, verbose_name="Фото страви")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено о")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Оновлено о")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Страва"
        verbose_name_plural = "Страви"


class Courier(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ім'я кур'єра")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено о")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Оновлено о")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Кур'єр"
        verbose_name_plural = "Кур'єри"