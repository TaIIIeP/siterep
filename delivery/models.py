from django.db import models
from django.db.models import Avg

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва категорії")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=150, verbose_name="Назва страви")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Ціна")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='dishes/', blank=True, null=True, verbose_name="Фото")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def average_rating(self):
        avg = self.ratings.aggregate(Avg('score'))['score__avg']
        return round(avg, 1) if avg else 0.0

    def __str__(self):
        return self.name

# Ось наші Кур'єри, яких я випадково загубив!
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

class Rating(models.Model):
    dish = models.ForeignKey(Dish, related_name='ratings', on_delete=models.CASCADE)
    score = models.IntegerField(verbose_name="Оцінка (1-5)")

class Subscriber(models.Model):
    email = models.EmailField(unique=True, verbose_name="Email для розсилки")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email