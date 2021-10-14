from django.contrib import admin
from .models import Ingredient, MenuItems, Customer, Purchase

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(MenuItems)
admin.site.register(Customer)
admin.site.register(Purchase)