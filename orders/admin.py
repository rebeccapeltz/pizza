from django.contrib import admin

# Register your models here.
from .models import Topping
from .models import PizzaMenu, SubsMenu, PastaMenu, SaladMenu,DinnerPlatterMenu
admin.site.register(Topping)
admin.site.register(PizzaMenu)
admin.site.register(SubsMenu)
admin.site.register(PastaMenu)
admin.site.register(SaladMenu)
admin.site.register(DinnerPlatterMenu)