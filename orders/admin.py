from django.contrib import admin

# Register your models here.
from .models import Topping
from .models import PizzaMenu, SubsMenu, PastaMenu, SaladMenu,DinnerPlatterMenu
from .models import Cart, CartItem
admin.site.register(Topping)
admin.site.register(PizzaMenu)
admin.site.register(SubsMenu)
admin.site.register(PastaMenu)
admin.site.register(SaladMenu)
admin.site.register(DinnerPlatterMenu)
admin.site.register(Cart)
admin.site.register(CartItem)