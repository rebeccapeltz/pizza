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
    path("orders/userorder", views.userorder, name="userorder"),
    path("<int:cartitem_id>/orders/cartitem/delete", views.cartitemdelete, name="cartitemdelete"),
    path("<int:orderitem_id>/orders/orderitem/delete", views.orderitemdelete, name="orderitemdelete"),
    path("<int:order_id>/orders/order/show", views.showorder, name="showorder"),
    path("<int:order_id>/orders/order/markcomplete", views.markcomplete, name="markcomplete"),
    path("orders/admin", views.admin, name="admin")
]
