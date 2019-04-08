from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal, ROUND_HALF_UP
from django.conf import settings

# Create your models here.

class PizzaMenu(models.Model):
  # Large/Small
  size = models.CharField(max_length=5)
  # Regular or Sicilian
  style = models.CharField(max_length=8)
  # Cheese, Special, 1 topping, 2 toppings or 3 toppings
  description = models.CharField(max_length=10)
  # price in cents
  price = models.IntegerField()


  def __str__(self):
    return f"{self.size} {self.style} Pizza: {self.description}  ${self.price_dollars()}"

  def price_dollars(self):
    return f"{Decimal(self.price/100).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)}"  

  def normalize(self):
    priceStr = str(self.price)
    return f"{self.size.lower()}-{self.style.lower()}-{self.description.lower()}-{priceStr}"

class PastaMenu(models.Model):
  description = models.CharField(max_length=50)
  price = models.IntegerField()
  def price_dollars(self):
    return f"{Decimal(self.price/100).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)}"  
  def __str__(self):
    return f"Pasta: {self.description}  ${self.price_dollars()}"
  def normalize(self):
    priceStr = str(self.price)
    return f"{self.description.lower()}-{priceStr}"

class DinnerPlatterMenu(models.Model):
# Small, Large, NA
  size = models.CharField(max_length=5)
  description = models.CharField(max_length=50)
  price = models.IntegerField() 
  def price_dollars(self):
    return f"{Decimal(self.price/100).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)}"  
  def __str__(self):
    return f"{self.size} Dinner Platter: {self.description}  ${self.price_dollars()}"
  def normalize(self):
    priceStr = str(self.price)
    return f"{self.description.lower()}-{priceStr}" 


class SaladMenu(models.Model):
  description = models.CharField(max_length=50)
  price = models.IntegerField()
  def price_dollars(self):
    return f"{Decimal(self.price/100).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)}"  
  def __str__(self):
    return f"Salad: {self.description}  ${self.price_dollars()}"
  def normalize(self):
    priceStr = str(self.price)
    return f"{self.description.lower()}-{priceStr}"


class SubsMenu(models.Model):
  # Small, Large, NA
  size = models.CharField(max_length=5)
  description = models.CharField(max_length=50)
  baseprice = models.IntegerField()

  def priceAdjustedForCheese(self):
    # add 50 cents cheese to base if true
    price = self.baseprice
    if cheese:
      price += 50
    return price

  def addCheese(self):
    return self.baseprice + 50

  def price_dollars(self):
    return f"{Decimal(self.baseprice/100).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)}"  
  def __str__(self):
    return f"{self.size} Subs: {self.description}  ${self.price_dollars()}"
  def normalize(self):
    priceStr = str(self.price)
    return f"{self.size.lower()}-{self.description.lower()}-{priceStr}"



# this is a reference table that supplies topping strings
class Topping(models.Model):
  description = models.CharField(max_length=25)

  def __str__(self):
    return f"{self.description}"

# there is only one cart per customer
# there are 0 or more items in the cart
class Cart(models.Model):
  #if customer deleted,  delete the cart
  customer = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.customer.username}"

  def cart_total_dollars(self):
    totalCents = 0
    all_cart_items = CartItem.objects.filter(cart=self).all()
    for item in all_cart_items:
      totalCents += item.price
    return f"{Decimal(totalCents/100).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)}"  


# access cart items from cart instance c.CartItem_set
class CartItem(models.Model):
  cart = models.ForeignKey(Cart, on_delete=models.CASCADE,blank=True, null=True,related_name="cart")
  quantity = models.IntegerField()
  # display = quantity <size> <style> description <toppings> @unit price_dollars total_price_dollars
  display = models.CharField(max_length=200,null=True)
  price = models.IntegerField()

  def price_dollars(self):
    return f"{Decimal(self.price/100).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)}"  

  def total_price_dollars(self):
    return f"{Decimal((self.price*self.quantity)/100).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)}"  

  def __str__(self):
    return self.display

class Order(models.Model):
  customer = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  status = models.CharField(max_length=10)
  def __str__(self):
    return f"Order ID: {self.id} Customer: {self.customer.username}  Status: {self.status}"

class OrderItem(models.Model):
  order = models.ForeignKey(Order, on_delete=models.CASCADE,blank=True, null=True,related_name="order")
  quantity = models.IntegerField()
  # display = quantity <size> <style> description <toppings> @unit price_dollars total_price_dollars
  display = models.CharField(max_length=200,null=True)
  price = models.IntegerField()

  def price_dollars(self):
    return f"{Decimal(self.price/100).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)}"  

  def total_price_dollars(self):
    return f"{Decimal((self.price*self.quantity)/100).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)}"  

  def __str__(self):
    return self.display