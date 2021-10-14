from django.shortcuts import render
from .models import Ingredient, MenuItems, Customer, Purchase
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import IngredientCreateForm, MenuItemsCreateForm, CustomerCreateForm, PurchaseCreateForm

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

# Models creation
class IngredientCreate(CreateView):
    model = Ingredient
    template_name = 'manager/model_creation_forms/add_ingredient.html'
    form_class = IngredientCreateForm

class MenuItemsCreate(CreateView):
    model = MenuItems
    template_name = 'manager/model_creation_forms/add_menu_item.html'
    form_class = MenuItemsCreateForm

class CustomerCreate(CreateView):
    model = Customer
    template_name = 'manager/model_creation_forms/add_customer.html'
    form_class = CustomerCreateForm