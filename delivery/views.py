


def home_view(request):
    context = {
        'title': 'Головна: Доставка їжі',
        'content': 'Вітаємо на сайті! Тут ви можете обрати найсмачнішу їжу.',
        'is_home': True
    }
    return render(request, 'delivery/page.html', context)


def about_view(request):
    context = {
        'title': 'Про нас',
        'content': 'Ми доставляємо їжу за 30 хвилин або безкоштовно!',
        'is_home': False
    }
    return render(request, 'delivery/page.html', context)


def contacts_view(request):
    context = {
        'title': 'Наші контакти',
        'content': 'Телефон: +38 (099) 123-45-67. Чекаємо на дзвінок!',
        'is_home': False
    }
    return render(request, 'delivery/page.html', context)


from django.shortcuts import render

# Create your views here.
