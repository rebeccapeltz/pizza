from django.urls import path

from . import views

urlpatterns = [
    path("", views.menu, name="menu"),
    path("orders/pizza/add", views.addpizza, name="addpizza"),
    path("orders/subs/add", views.addsub, name="addsub"),
    path("orders/pasta/add", views.addpasta, name="addpasta"),
    path("orders/salad/add", views.addsalad, name="addsalad"),
    path("orders/dinnerplatter/add", views.adddinnerplatter, name="adddinnerplatter"),
    path("orders/cart", views.usercart, name="usercart"),
    path("orders/checkout", views.checkout, name="checkout"),
    path("<int:cartitem_id>/orders/cartitem/delete", views.cartitemdelete, name="cartitemdelete")
]
