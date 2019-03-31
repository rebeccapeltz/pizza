from django.http import HttpResponse
from django.shortcuts import render
from .models import Topping, PizzaMenu
# import logging
# logger = logging.getLogger(__name__)


# Create your views here.
def index(request):
  pizzas = PizzaMenu.objects.all()
  context = {
        "toppings": Topping.objects.all(),
        "pizzas": pizzas
    }
  # logger.info(pizzas)
  return render(request, "orders/index.html", context)
  # return HttpResponse("Project 3: TODO")

def addpizza(request):
  size = request.POST["size"]
  style = request.POST["style"]
  description = request.POST["description"]
  price = int(request.POST["price"])
  context = {
    "size":size,
    "style":style,
    "description":description,
    "price":price
  }
  return render(request, "orders/cart.html", context)

