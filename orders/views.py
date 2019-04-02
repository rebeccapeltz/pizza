from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .models import Topping, PizzaMenu, SubsMenu
from .models import Cart, CartItem
from decimal import Decimal, ROUND_HALF_UP
from django.forms.models import model_to_dict
from django.urls import reverse


# import logging
# logger = logging.getLogger(__name__)

#helper function to integer cents into dollar string
def price_dollars(price):
  return f"{Decimal(price/100).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)}"  

def total_dollars(price, quantity):
  return f"{Decimal(price*quantity/100).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)}"  

# Create your views here.
def menu(request):
  pizzas = PizzaMenu.objects.all()
  subs = SubsMenu.objects.all()
  context = {
        "toppings": Topping.objects.all(),
        "pizzas": pizzas,
        "subs": subs
    }
  # logger.info(pizzas)
  return render(request, "orders/index.html", context)

#TODO add salads
#TODO add pasta
#TODO add dinner platters

#TODO fininsh
def addsub(request):
  subid = request.POST["selectedsubid"]
  subObj = SubsMenu.objects.get(pk=subid)
  context = {}
  return render(request, "orders/cart.html", context)

# get current user and show their cart
def usercart(request):
  current_user = request.user
  cart = None
  for c in Cart.objects.all():
    if c.customer.username == current_user.username:
      print (c.customer.username)
      cart = c
      break
  customer = c.customer
  print(f"username: {customer.username}")
  if cart is not None:
    all_cart_items = CartItem.objects.filter(cart=cart).all()
    context = {
      "customer":model_to_dict(customer),
      "cartitems":all_cart_items.values()
    }
  else:
    context = {
      "cart":None,
      "cartitems":None
    }
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

  # create a cart item and add to cart
  if cart is None:
    cart = Cart(customer=current_user)
    cart.save()
  # create a context with cart and cart items
  cart_item = CartItem(quantity=quantity, display=display, price=price, cart=cart)
  cart_item.save()
  all_cart_items = CartItem.objects.filter(cart=cart).all()
  customer = c.customer

  context = {
    "customer":model_to_dict(customer),
    "cartitems":all_cart_items.values()
  }
# Passenger.objects.exclude(flights=flight).all()
  return render(request, "orders/cart.html", context)

# delete cart item
def cartitemdelete(request, cartitem_id):
  # try:
  cart_item = None
  cart_items = CartItem.objects.all()
  for item in cart_items:
    if item.id == cartitem_id:
      cart_item = item
      break
  if cart_item is None:
    return render(request,"orders/error.html", {"message":"No cart item found to delete"})
  else:
    cart_item.delete()
  return HttpResponseRedirect(reverse("usercart"))



# TODO place order copy cart to order and delete cart

# TODO orders page fulfilled vs open