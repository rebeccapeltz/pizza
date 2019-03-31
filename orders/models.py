from django.db import models
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

class Topping(models.Model):
  description = models.CharField(max_length=25)

  def __str__(self):
    return f"{self.description}"

