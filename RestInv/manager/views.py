from django.shortcuts import render
from .models import Ingredient, MenuItems, Customer, Purchase
from django.views.generic import ListView
from .forms import IngredientCreateForm

# Create your views here.

# home function
def home(request):
    context = {"hello": "hello world!"}
    return render(request, "manager/home.html", context)

# Showing Models
class IngredientList(ListView):
    model = Ingredient
    template_name = "manager/lists/ingredients.html"

class MenuItemsList(ListView):
    model = MenuItems
    template_name = "manager/lists/menu_items.html"

class CustomerList(ListView):
    model = Customer
    template_name = "manager/lists/customers.html"

class PurchaseList(ListView):
    model = Purchase
    template_name = "manager/lists/purchases.html"