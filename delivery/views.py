from django.shortcuts import render
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
        # ОНОВЛЕНИЙ ТЕКСТ БЕЗ ЛАБИ
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