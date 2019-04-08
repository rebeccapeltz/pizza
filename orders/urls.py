from django.urls import path

from . import views

urlpatterns = [
    path("", views.menu, name="menu"),
    path("orders/pizza/add", views.addpizza, name="addpizza"),
    path("orders/subs/add", views.addsub, name="addsub"),
    path("orders/pasta/add", views.addpasta, name="addpasta"),
    path("orders/salad/add", views.addpasta, name="addsalad"),
    path("orders/dinnerplatter/add", views.addpasta, name="adddinnerplatter"),
    path("orders/cart", views.usercart, name="usercart"),
    path("<int:cartitem_id>/orders/cartitem/delete", views.cartitemdelete, name="cartitemdelete")
  
]
#  path("<int:flight_id>/book", views.book, name="book")
  # path("order/cart/delete/")
#   "{% url 'book' flight.id %}"
# "{% url 'orders/cart/delete' cartitem.id %}"