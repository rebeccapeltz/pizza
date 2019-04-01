from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal, ROUND_HALF_UP

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




class Topping(models.Model):
  description = models.CharField(max_length=25)

  def __str__(self):
    return f"{self.description}"

class CartItem(models.Model):
  quantity = models.IntegerField()
  size = models.IntegerField()
  style = models.CharField(max_length=8)
  description = models.CharField(max_length=10)
  toppings = models.CharField(max_length=50)
  unitPrice = models.IntegerField()

  def price_dollars(self):
    return f"{Decimal(self.price/100).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)}"  

  def total_price_dollars(self):
    return f"{Decimal((self.price*self.quantity)/100).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)}"  

# there is only one cart per customer
# there are 0 or more items in the cart
class Cart(models.Model):
  customer = models.ForeignKey(User, on_delete=models.CASCADE,related_name="customer")
  #TODO is there a one to many
  cartitems = models.ManyToManyField(CartItem, blank=True, related_name="cartitems")


