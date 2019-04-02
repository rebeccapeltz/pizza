from django.urls import path

from . import views

urlpatterns = [
    path("orders/menu", views.menu, name="menu"),
    path("orders/pizza/add", views.addpizza, name="addpizza"),
    path("order/subs/add", views.addsub, name="addsub"),
    path("order/cart", views.usercart, name="usercart")
]
