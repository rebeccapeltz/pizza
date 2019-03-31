from django.contrib import admin

# Register your models here.
from .models import Topping
from .models import PizzaMenu

admin.site.register(Topping)
admin.site.register(PizzaMenu)
