from django.http import HttpResponse
from django.shortcuts import render
from .models import Topping, PizzaMenu, SubsMenu
from .models import Cart, CartItem
from decimal import Decimal, ROUND_HALF_UP
from django.forms.models import model_to_dict

# import logging
# logger = logging.getLogger(__name__)

#helper function to integer cents into dollar string
def price_dollars(price):
  return f"{Decimal(price/100).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)}"  

def total_dollars(price, quantity):
  return f"{Decimal(price*quantity/100).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)}"  

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
  quantity = int(request.POST["pizza-qty"])
  context = {
    "size":size,
    "style":style,
    "description":description,
    "price":price,
    "toppings":toppings,
    "quantity":quantity
  }
  # create display for the item so you can use the str for the display
  if len(toppings)>0:
    display = f"Pizza: {size} {style} {description} {toppings} {quantity}@${price_dollars(price)} ${total_dollars(price,quantity)}"
  else:
    display = f"Pizza: {size} {style} {description} {quantity}@${price_dollars(price)}  ${total_dollars(price,quantity)}"

  # get the user/customer
  current_user = request.user
  # see if there is a cart for the customer/create one if not
  # cart = Cart.objects.filter( customer.id == current_user.id)
  # get all carts
  cart = None
  for c in Cart.objects.all():
    if c.customer.username == current_user.username:
      print (c.customer.username)
      cart = c
      break 

  # cart = Cart.objects.filter(customer.username == current_user.username)
  # cart = carts.filter(customer.username == current_user.username)

  # create a cart item and add to cart
  if cart is None:
    cart = Cart(customer=current_user)
    cart.save()
  # create a context with cart and cart items
  cart_item = CartItem(quantity=quantity, display=display, price=price, cart=cart)
  cart_item.save()



 

  # cart.user, cart.cart_items .quantity  .display . price
  # A.objects.filter(b = b) 
  # items = Cart.objects.filter(cart_item__customer.id = current_user.id)
  all_cart_items = CartItem.objects.filter(cart=cart).all()
  # for item in all_cart_items:
  #   print(f"{item.id} {item.display}")
  context = {
    "cart":model_to_dict(cart),
    "cart_item":all_cart_items.values()
  }
# Passenger.objects.exclude(flights=flight).all()
  return render(request, "orders/cart.html", context)

