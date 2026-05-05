from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Dish, Rating, Subscriber


# Допоміжна функція, яка рахує кількість товарів у кошику
def get_cart_count(request):
    return len(request.session.get('cart', []))


def home_view(request):
    context = {
        'title': 'Головна сторінка',
        'categories': Category.objects.all(),
        'dishes': Dish.objects.all(),
        'is_home': True,
        'cart_count': get_cart_count(request)  # Передаємо лічильник
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

        Ми використовуємо лише свіжі інгредієнти та перевірені рецепти. 
        Дякуємо, що обираєте нас!
        ''',
        'is_home': False,
        'cart_count': get_cart_count(request)  # Передаємо лічильник
    }
    return render(request, 'delivery/page.html', context)


def contacts_view(request):
    context = {
        'title': 'Контакти',
        'categories': Category.objects.all(),
        'content': 'Телефонуйте для замовлення: +38 (099) 123-45-67',
        'is_home': False,
        'cart_count': get_cart_count(request)  # Передаємо лічильник
    }
    return render(request, 'delivery/page.html', context)


def category_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    context = {
        'title': f'Меню: {category.name}',
        'categories': Category.objects.all(),
        'dishes': Dish.objects.filter(category=category),
        'is_category': True,
        'current_category': category,
        'cart_count': get_cart_count(request)  # Передаємо лічильник
    }
    return render(request, 'delivery/page.html', context)


def dish_view(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)

    if request.method == 'POST' and 'score' in request.POST:
        score = int(request.POST.get('score'))
        if 1 <= score <= 5:
            Rating.objects.create(dish=dish, score=score)
        return redirect('dish', dish_id=dish.id)

    context = {
        'title': dish.name,
        'categories': Category.objects.all(),
        'dish': dish,
        'is_dish': True,
        'cart_count': get_cart_count(request)  # Передаємо лічильник
    }
    return render(request, 'delivery/page.html', context)


def add_to_cart(request, dish_id):
    cart = request.session.get('cart', [])
    cart.append(dish_id)
    request.session['cart'] = cart
    # ОНОВЛЕНО: Тепер не кидає в кошик, а залишає на тій самій сторінці!
    return redirect(request.META.get('HTTP_REFERER', 'home'))


def cart_view(request):
    if request.method == 'POST' and 'clear' in request.POST:
        request.session['cart'] = []
        return redirect('cart')

    cart_ids = request.session.get('cart', [])
    cart_items = []
    total = 0
    for d_id in cart_ids:
        dish = Dish.objects.filter(id=d_id).first()
        if dish:
            cart_items.append(dish)
            total += dish.price

    context = {
        'title': 'Ваш Кошик',
        'categories': Category.objects.all(),
        'cart_items': cart_items,
        'total': total,
        'is_cart': True,
        'cart_count': len(cart_ids)  # Передаємо лічильник
    }
    return render(request, 'delivery/page.html', context)


def subscribe_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            Subscriber.objects.get_or_create(email=email)
    return redirect(request.META.get('HTTP_REFERER', 'home'))