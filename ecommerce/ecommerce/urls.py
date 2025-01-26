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
    path('register/',registerUser,name="registerUser"),
    path('logout/',LogoutUser,name="LogoutUser"),

    path('cart/add/<slug:slug>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<slug:slug>/', remove_from_cart, name='remove_from_cart'),
    path('cart/',view_cart, name='view_cart'),
    path('order/',place_order,name='place_order'),
    path('orderlist/',order_list,name="order_list"),
    path('cart/update/<int:items_id>/<str:action>/', cart_items_increase, name='cart_items_increase'),
    # path('orderdetail/<int:order_id>/',order_detail,name="order_detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)