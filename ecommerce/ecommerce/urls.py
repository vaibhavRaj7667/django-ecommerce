"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import*
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',LoginUser,name='LoginUser'),
    path('home/',Home,name="Home"),
    path('home/<slug:slug>/', Home, name='home_with_slug'),
    path('products/<slug:slug>/',products,name="products"),
    path('products/<slug:slug>/<int:price>/',products, name='products_by_price'),
    path('items/<slug:slug_>/',items,name="items"),

    path('cart/add/<slug:slug>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<slug:slug>/', remove_from_cart, name='remove_from_cart'),
    path('cart/',view_cart, name='view_cart'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)