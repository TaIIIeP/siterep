from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from delivery import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Адмінка
    path('admin/', admin.site.urls),

    # Основні сторінки сайту
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('contacts/', views.contacts_view, name='contacts'),

    # Каталог та товари
    path('category/<int:category_id>/', views.category_view, name='category'),
    path('dish/<int:dish_id>/', views.dish_view, name='dish'),

    # Кошик та розсилка
    path('cart/', views.cart_view, name='cart'),
    path('add-to-cart/<int:dish_id>/', views.add_to_cart, name='add_to_cart'),
    path('subscribe/', views.subscribe_view, name='subscribe'),

    # Авторизація та особистий кабінет (Лаба 8)
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='delivery/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile_view, name='profile'),

    # Системні шляхи Django для відновлення пароля (відправка email тощо)
    path('accounts/', include('django.contrib.auth.urls')),
    path('remove-from-cart/<int:dish_id>/', views.remove_from_cart, name='remove_from_cart'),
]

# Цей блок дозволяє Django правильно показувати картинки (media) під час розробки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)