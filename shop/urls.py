"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from mysite import views as mv
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',mv.home,name="home"),
    path('login/', mv.logins, name = "login"),
    ##path('login/', mv.login_view, name='login'),
     path('evaluate/<int:product_id>/', mv.evaluate, name='evaluate'),
    path("product/<int:id>", mv.showproduct, name="product"),
    path('mine/',mv.mine,name="mine"),
    path('man/',mv.man,name="man"),
    path('girl/',mv.girl,name="girl"),
    path('child/',mv.child,name="child"),
    path('jewelry/',mv.jewelry,name="jewelry"),
    path('shoe/',mv.shoe,name="shoe"),
    path('shopcar/',mv.shopcar,name="shopcar"),
    # path('register/',mv.register,name="register"),
    path('register/',mv.register,name="register"),
    path('order/',mv.order,name="order"),
    path('search/',mv.search,name="search"),
    path('masearch/',mv.masearch,name="masearch"),
    path('logout/',mv.logout,name='logout'),
    path('pay/',mv.pay,name="pay"),
    path('profile/',mv.profile,name='profile'),
    # path('product/', mv.product, name='product_list'),
    path('add-to-cart/<int:product_id>/', mv.add_to_cart, name='add_to_cart'),
    path('manage/',mv.manage,name='manage'),
    path('change/',mv.change,name='change'),
    path('inventory/', mv.inventory, name='inventory'),
    path('add_stock/<int:product_id>/', mv.add_stock, name='add_stock'),
    path('clear_cart/', mv.clear_cart, name='clear_cart'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
