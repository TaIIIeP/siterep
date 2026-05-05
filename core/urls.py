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

    # Шляхи для Лаби 6 (Окрема категорія і Окремий товар)
    path('category/<int:category_id>/', views.category_view, name='category'),
    path('dish/<int:dish_id>/', views.dish_view, name='dish'),
]

# Дозволяємо відображення картинок на сайті
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)