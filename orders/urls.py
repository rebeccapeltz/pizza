from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("orders/pizza/add", views.addpizza, name="addpizza")
]
