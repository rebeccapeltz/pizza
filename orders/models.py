from django.db import models

# Create your models here.
class Topping(models.Model):
  description = models.CharField(max_length=25)

  def __str__(self):
    return f"{self.description}"