from django.http import HttpResponse
from django.shortcuts import render
from .models import Topping, PizzaMenu, SubsMenu
# import logging
# logger = logging.getLogger(__name__)


# Create your views here.
def index(request):
  pizzas = PizzaMenu.objects.all()
  subs = SubsMenu.objects.all()
  context = {
        "toppings": Topping.objects.all(),
        "pizzas": pizzas,
        "subs": subs
    }
  # logger.info(pizzas)
  return render(request, "orders/index.html", context)
  # return HttpResponse("Project 3: TODO")

def addsub(request):
  subid = request.POST["selectedsubid"]
  subObj = SubsMenu.objects.get(pk=subid)
  context = {}
  return render(request, "orders/cart.html", context)

def addpizza(request):
  size = request.POST["size"]
  style = request.POST["style"]
  description = request.POST["description"]
  price = int(request.POST["price"])
  toppings = request.POST["toppings"]
  quantity = request.POST["pizza-qty"]
  context = {
    "size":size,
    "style":style,
    "description":description,
    "price":price,
    "toppings":toppings,
    "quantity":quantity
  }
  # get the user/customer
  user = request.user
  # see if there is a cart for the customer/create on if not
  # ?? how to look up cart based on user
  # if (Cart.objects.get(pk=cart_id))

  # create a item in the cart using this data
  # set context to be the whole cart
  return render(request, "orders/cart.html", context)

