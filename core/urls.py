from django.contrib import admin
from django.urls import path
from delivery import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('contacts/', views.contacts_view, name='contacts'),
    path('category/<int:category_id>/', views.category_view, name='category'),
    path('dish/<int:dish_id>/', views.dish_view, name='dish'),

    # НОВІ ШЛЯХИ ДЛЯ ЛАБИ 7
    path('cart/', views.cart_view, name='cart'),
    path('add-to-cart/<int:dish_id>/', views.add_to_cart, name='add_to_cart'),
    path('subscribe/', views.subscribe_view, name='subscribe'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)