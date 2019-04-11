from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .models import Topping, PizzaMenu, SubsMenu, PastaMenu, DinnerPlatterMenu, SaladMenu
from .models import Cart, CartItem, Order, OrderItem
from decimal import Decimal, ROUND_HALF_UP
from django.forms.models import model_to_dict
from django.urls import reverse


#helper function to integer cents into dollar string
def price_dollars(price):
  return f"{Decimal(price/100).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)}"  

def total_dollars(price, quantity):
  return f"{Decimal(price*quantity/100).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)}"  

# Create your views here.
def menu(request):
  if ((request.user is not None) and (request.user.is_active == True)):
    pizzas = PizzaMenu.objects.all()
    subs = SubsMenu.objects.all()
    pastas = PastaMenu.objects.all()
    dinnerplatters = DinnerPlatterMenu.objects.all()
    salads = SaladMenu.objects.all()
    context = {
          "toppings": Topping.objects.all(),
          "pizzas": pizzas,
          "subs": subs,
          "pastas":pastas,
          "dinnerplatters": dinnerplatters,
          "salads": salads,
          "user": request.user
      }
    return render(request, "orders/index.html", context)
  else:
     return render(request, 'users/login.html', {"message":"You need to login to access menu."})

#TODO add salads
def addsalad(request):
  saladid = request.POST["select-salad"]
  saladObj = SaladMenu.objects.get(pk=saladid)
  quantity = int(request.POST["salad-qty"])
  display = f"Salds: {saladObj.description} {quantity}@${price_dollars(saladObj.price)} ${total_dollars(saladObj.price,quantity)}"

  cart = cartAdd(request, quantity, display, saladObj.price)
  all_cart_items = CartItem.objects.filter(cart=cart).all()
  context = {
    "customer":model_to_dict(cart.customer),
    "cart":cart.cart_total_dollars(),
    "cartitems":all_cart_items.values(),
    "cartIsEmpty": (len(all_cart_items) == 0),
    "user": request.user
  }
  return render(request, "orders/cart.html", context)


#TODO add pasta
def addpasta(request):
  pastaid = request.POST["select-pasta"]
  pastaObj = PastaMenu.objects.get(pk=pastaid)
  quantity = int(request.POST["pasta-qty"])
  display = f"Pasta: {pastaObj.description} {quantity}@${price_dollars(pastaObj.price)} ${total_dollars(pastaObj.price,quantity)}"

  cart = cartAdd(request, quantity, display, pastaObj.price)
  all_cart_items = CartItem.objects.filter(cart=cart).all()
  context = {
    "customer":model_to_dict(cart.customer),
    "cart":cart.cart_total_dollars(),
    "cartitems":all_cart_items.values(),
    "cartIsEmpty": (len(all_cart_items) == 0),
    "user": request.user
  }
  return render(request, "orders/cart.html", context)


#TODO add dinner platters
def adddinnerplatter(request):
  dinnerplatterid = request.POST["select-dinnerplatter"]
  dinnerPlatterObj = DinnerPlatterMenu.objects.get(pk=dinnerplatterid)
  quantity = int(request.POST["dinnerplatter-qty"])
  dinnerPlatterObj = DinnerPlatterMenu.objects.get(pk=dinnerplatterid)
  price = dinnerPlatterObj.price
  display = f"Dinner Platter: {dinnerPlatterObj.description} {quantity}@${price_dollars(price)} ${total_dollars(price,quantity)}"
  cart = cartAdd(request, quantity, display, price)
  all_cart_items = CartItem.objects.filter(cart=cart).all()
  context = {
    "customer":model_to_dict(cart.customer),
    "cart":cart.cart_total_dollars(),
    "cartitems":all_cart_items.values(),
    "cartIsEmpty": (len(all_cart_items) == 0),
    "user": request.user
  }
  return render(request, "orders/cart.html", context)


def addsub(request):
  subid = request.POST["select-sub"]
  quantity = int(request.POST["sub-qty"])
  try:
    cheese = request.POST["addcheese"]
  except Exception:
    cheese = False
  subObj = SubsMenu.objects.get(pk=subid)
  price = subObj.baseprice
  displayCheese = ''
  if cheese == 'True':
    price += 50
    displayCheese = "Extra Cheese"
  pricedollars = price_dollars(price)
  display = f"Sub: {subObj.size} {displayCheese} {subObj.description} {quantity}@${price_dollars(price)} ${total_dollars(price,quantity)}"

  cart = cartAdd(request, quantity, display, price)
  all_cart_items = CartItem.objects.filter(cart=cart).all()

  context = {
     "customer":model_to_dict(cart.customer),
      "cart":cart.cart_total_dollars(),
      "cartitems":all_cart_items.values(),
      "cartIsEmpty": (len(all_cart_items) == 0),
      "user": request.user
  }
  return render(request, "orders/cart.html", context)

# get current user and show their cart
def usercart(request):
  if ((request.user is not None) and (request.user.is_active == True)):
    current_user = request.user
    cart = None
    for c in Cart.objects.all():
      if c.customer.username == current_user.username:
        print (c.customer.username)
        cart = c
        break
    
    if cart is not None:
      customer = cart.customer
      print(f"username: {customer.username}")
      all_cart_items = CartItem.objects.filter(cart=cart).all()
      cartIsEmpty = (len(all_cart_items) == 0)
      context = {
        "customer":model_to_dict(customer),
        "cart":cart.cart_total_dollars(),
        "cartitems":all_cart_items.values(),
        "cartIsEmpty": cartIsEmpty,
        "user": request.user
      }
    else:
      context = {
        "customer":None,
        "cart":0,
        "cartitems":None,
        "cartIsEmpty": True,
        "user": request.user
      }
    return render(request, "orders/cart.html", context)
  else:
    return render(request, 'users/login.html', {"message":"You need to login to access cart."})


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
    "quantity":quantity,
     "user": request.user
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
  customer = cart.customer

  context = {
    "customer":model_to_dict(customer),
    "cart":cart.cart_total_dollars(),
    "cartitems":all_cart_items.values(),
     "user": request.user
  }
  return render(request, "orders/cart.html", context)

# add to cart
def cartAdd(request, quantity, display, price):
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
  return cart

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
    return render(request,"orders/error.html", {"message":"No cart item found to delete", "user": request.user})
  else:
    cart_item.delete()
  return HttpResponseRedirect(reverse("usercart"))

def orderitemdelete(request, orderitem_id):
  # try:
  order_item = None
  order_items = OrderItem.objects.all()
  for item in order_items:
    if item.id == orderitem_id:
      order_item = item
      break
  if order_item is None:
    return render(request,"orders/error.html", {"message":"No order item found to delete", "user": request.user})
  else:
    order_item.delete()
  return HttpResponseRedirect(reverse("userorder"))


# checkout/place order copy cart to order and delete cart
def checkout(request):
  # guard against non-authenticated user
  if ((request.user is not None) and (request.user.is_active == True)):
    current_user = request.user

    # start with getting cart and it's items
    # and for each item in cart create an order item
    cart = None
    for c in Cart.objects.all():
      if c.customer.username == current_user.username:
        print (f"creating order from cart{c.customer.username}")
        cart = c
        break 
    # if there is no cart send to error (shouldn't get here from UI)
    cartitems = None
    if cart is None:
      return render(request, "orders/error.html", {"message":"You cannot create an order from an empty cart", "user": request.user})

    else:
      # get cart items
      cart_items = CartItem.objects.all()

    #retrieve or create an order
    order = None
    for o in Order.objects.all():
      if o.customer.username == current_user.username:
        print (o.customer.username)
        order = o
        break

    if order is None:
      #create order
      order = Order(customer=current_user)
      order.save()

    # add cart items to order
    for cartitem in cart_items:
      order_item = OrderItem(quantity=cartitem.quantity, display=cartitem.display, price=cartitem.price, order=order)
      order_item.save()
      # remove cart item as you add to order
      cartitem.delete()
   
    # test for empty order
    orderIsEmpty = (len(cart_items) == 0)
    
    # provide different context for order without any items
    if orderIsEmpty:
      context = {
        "customer":order.customer,
        "order_total":"$0.00",
        "order_id":None,
        "orderIsEmpty": True,
        "user": request.user
      }
    else:
      customer = order.customer
      all_order_items = OrderItem.objects.filter(order=order).all()
      total_cents = 0
      for item in all_order_items:
        total_cents += item.quantity * item.price
      total_order_amount_display = price_dollars(total_cents)
      context = {
        "customer":model_to_dict(customer),
        "order_total":total_order_amount_display,
        "order_id":order.id,
        "orderitems":all_order_items.values(),
        "orderIsEmpty": False,
        "user": request.user
      }
    return render(request, "orders/order.html", context)
  else:
    return render(request, 'users/login.html', {"message":"You need to login to access order."})

def userorder(request):
  if ((request.user is not None) and (request.user.is_active == True)):
    current_user = request.user

    #retrieve or create an order
    order = None
    for o in Order.objects.all():
      if o.customer.username == current_user.username:
        print (o.customer.username)
        order = o
        break
    
    # if no order send to error
    if order is None:
      return render(request,"orders/error.html", {"message":"No cart item found to delete", "user": request.user})
    else:
      # provide different context for order without any items
      # test for empty order
      all_order_items = OrderItem.objects.filter(order=order).all()
      orderIsEmpty = (len(all_order_items) == 0)

      if orderIsEmpty:
        context = {
          "customer":order.customer,
          "order_total":"$0.00",
          "order_id":None,
          "orderIsEmpty": True,
          "user": request.user
        }
      else:
        customer = order.customer
        total_cents = 0
        for item in all_order_items:
          total_cents += (item.quantity * item.price)
        total_order_amount_display = price_dollars(total_cents)
        context = {
          "customer":model_to_dict(customer),
          "order_total":total_order_amount_display,
          "order_id":order.id,
          "orderitems":all_order_items.values(),
          "orderIsEmpty": False,
          "user": request.user
        }
      return render(request, "orders/order.html", context)

  else:
    return render(request, 'users/login.html', {"message":"You need to login to access order."})

def fullname(fname, lname, username):
  if fname == "" and lname == "":
    return username
  else:
    return fname + " " + lname

# admin page where super user can mark order status complete
def admin(request):
  if ((request.user is not None) and (request.user.is_superuser == True)):
    orders = []
    order_completed_total_cents = 0
    order_pending_total_cents = 0

    # get all orders and calculate completed and pending totals
    # also prepare data for binding to template
    orders_data = Order.objects.all()
  
    for order_data in orders_data:
      order = {
        "id":order_data.id,
        "status": order_data.status,
        "customer_name":fullname(order_data.customer.first_name,order_data.customer.last_name,order_data.customer.username)
      }
      orders.append(order)
      order_items_data = OrderItem.objects.filter(order=order_data).all()
      if order_data.status == "Complete":
        for item in order_items_data:
          order_completed_total_cents += (item.quantity * item.price)
      else:
        for item in order_items_data:
          order_pending_total_cents += (item.quantity * item.price)

    #order. status, id, display
    context= {
      "orders":orders,
      "order_pending_total":price_dollars(order_pending_total_cents),
      "order_completed_total":price_dollars(order_completed_total_cents)}
    return render(request,"orders/admin.html",context)
  else:
    return render(request,"orders/error.html", {"message":"You need admin rights to view the admin page", "user": request.user})
 

# show order by id from admin page
def showorder(request, order_id):
  # security
  print(f"{order_id} was requested to be shown to user {request.user}")
  if ((request.user is not None) and (request.user.is_superuser == True)):
    order = Order.objects.get(pk=order_id)
    customer = order.customer
    all_order_items = OrderItem.objects.filter(order=order).all()
    total_cents = 0
    for item in all_order_items:
      total_cents += item.quantity * item.price
    total_order_amount_display = price_dollars(total_cents)
    context = {
      "customer":model_to_dict(customer),
      "order_total":total_order_amount_display,
      "order_id":order.id,
      "orderitems":all_order_items.values(),
      "orderIsEmpty": False,
      "user": request.user
    }
    return render(request,"orders/order.html",context)
  else:
    return render(request,"orders/error.html", {"message":"You need admin rights to view a customer order page", "user": request.user})
  

def markcomplete(request, order_id):
  print(order_id)
  # get the order and set status to "Complete"
   # security
  print(f"{order_id} was requested to be shown to user {request.user}")
  if ((request.user is not None) and (request.user.is_superuser == True)):
    order = Order.objects.get(pk=order_id)
    order.status = "Complete"
    order.save()
    return HttpResponseRedirect(reverse("admin"))

  else:
    return render(request,"orders/error.html", {"message":"You need admin rights to view a customer order page", "user": request.user})
  