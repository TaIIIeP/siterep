from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Category, Dish, Order
from .forms import ExtendedUserCreationForm, UserProfileForm


# ПРАВИЛЬНИЙ підрахунок кількості страв у кошику
def get_cart_count(request):
    cart = request.session.get('cart', {})
    # Якщо кошик — це список (старий формат), очищуємо його
    if not isinstance(cart, dict):
        request.session['cart'] = {}
        return 0
    return sum(cart.values())


def home_view(request):
    dishes = Dish.objects.all().order_by('category__name', 'name')
    return render(request, 'delivery/page.html', {
        'title': 'Меню', 'categories': Category.objects.all(),
        'dishes': dishes, 'is_home': True, 'cart_count': get_cart_count(request)
    })


def category_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    dishes = Dish.objects.filter(category=category).order_by('name')
    return render(request, 'delivery/page.html', {
        'title': category.name, 'categories': Category.objects.all(),
        'dishes': dishes, 'is_category': True, 'cart_count': get_cart_count(request)
    })


def dish_view(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    return render(request, 'delivery/page.html', {
        'title': dish.name, 'categories': Category.objects.all(),
        'dish': dish, 'is_dish': True, 'cart_count': get_cart_count(request)
    })


def cart_view(request):
    cart = request.session.get('cart', {})

    # ЗАХИСТ: Якщо кошик залишився старим списком — перетворюємо на порожній словник
    if not isinstance(cart, dict):
        cart = {}
        request.session['cart'] = {}

    cart_items = []
    total = 0

    for dish_id, quantity in cart.items():
        dish = Dish.objects.filter(id=int(dish_id)).first()
        if dish:
            s = dish.price * quantity
            total += s
            cart_items.append({'dish': dish, 'quantity': quantity, 'item_total': s})

    if request.method == 'POST':
        if 'checkout' in request.POST:
            if not request.user.is_authenticated: return redirect('login')
            addr = request.POST.get('address')
            if cart_items and addr:
                txt = ", ".join([f"{i['dish'].name} x{i['quantity']}" for i in cart_items])
                Order.objects.create(user=request.user, items_text=txt, total_price=total, address=addr)
                request.session['cart'] = {}
                return redirect('profile')
        elif 'clear' in request.POST:
            request.session['cart'] = {}
            return redirect('cart')

    return render(request, 'delivery/page.html', {
        'title': 'Кошик', 'cart_items': cart_items, 'total': total,
        'is_cart': True, 'categories': Category.objects.all(), 'cart_count': get_cart_count(request)
    })


def add_to_cart(request, dish_id):
    cart = request.session.get('cart', {})
    if not isinstance(cart, dict): cart = {}
    d_id = str(dish_id)
    cart[d_id] = cart.get(d_id, 0) + 1
    request.session['cart'] = cart
    return redirect(request.META.get('HTTP_REFERER', 'home'))


def remove_from_cart(request, dish_id):
    cart = request.session.get('cart', {})
    if not isinstance(cart, dict): cart = {}
    d_id = str(dish_id)
    if d_id in cart:
        if cart[d_id] > 1:
            cart[d_id] -= 1
        else:
            del cart[d_id]
    request.session['cart'] = cart
    return redirect('cart')


def register_view(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = ExtendedUserCreationForm()
    return render(request, 'delivery/register.html',
                  {'form': form, 'title': 'Реєстрація', 'categories': Category.objects.all()})


@login_required
def profile_view(request):
    if request.method == 'POST':
        f = UserProfileForm(request.POST, instance=request.user)
        if f.is_valid(): f.save(); return redirect('profile')
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'delivery/profile.html', {
        'orders': orders, 'profile_form': UserProfileForm(instance=request.user),
        'categories': Category.objects.all(), 'cart_count': get_cart_count(request)
    })


def about_view(request):
    return render(request, 'delivery/page.html',
                  {'title': 'Про нас', 'categories': Category.objects.all(), 'content': 'Смачно!',
                   'cart_count': get_cart_count(request)})


def contacts_view(request):
    return render(request, 'delivery/page.html',
                  {'title': 'Контакти', 'categories': Category.objects.all(), 'content': '+380...',
                   'cart_count': get_cart_count(request)})


def subscribe_view(request):
    return redirect('home')