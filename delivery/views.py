from django.shortcuts import render, get_object_or_404
from .models import Category, Dish

def home_view(request):
    context = {
        'title': 'Головна сторінка',
        'categories': Category.objects.all(),
        'dishes': Dish.objects.all(),
        'is_home': True
    }
    return render(request, 'delivery/page.html', context)

def about_view(request):
    context = {
        'title': 'Про нас',
        'categories': Category.objects.all(),
        'content': '''
        Ми — "Доставка від Паші", найшвидший сервіс у місті Луцьк! 
        Готуємо з любов'ю та доставляємо гарячим прямісінько до ваших дверей. 
        Наші кур'єри знають кожну вулицю міста, тому ваша піца ніколи не охолоне. 
        ''',
        'is_home': False
    }
    return render(request, 'delivery/page.html', context)

def contacts_view(request):
    context = {
        'title': 'Наші контакти',
        'categories': Category.objects.all(),
        'content': 'Телефонуйте для замовлення: +38 (099) 123-45-67',
        'is_home': False
    }
    return render(request, 'delivery/page.html', context)

# --- НОВІ ФУНКЦІЇ ДЛЯ ЛАБИ 6 ---

def category_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    context = {
        'title': f'Меню: {category.name}',
        'categories': Category.objects.all(),
        'dishes': Dish.objects.filter(category=category), # Показуємо товари ТІЛЬКИ цієї категорії
        'is_category': True,
        'current_category': category
    }
    return render(request, 'delivery/page.html', context)

def dish_view(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    context = {
        'title': dish.name,
        'categories': Category.objects.all(),
        'dish': dish,
        'is_dish': True
    }
    return render(request, 'delivery/page.html', context)