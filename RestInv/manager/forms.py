from .models import Ingredient, MenuItems, Customer, Purchase
from django import forms

# Forms for creating models
class IngredientCreateForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"

class MenuItemsCreateForm(forms.ModelForm):
    class Meta:
        model = MenuItems
        fields = "__all__"

class CustomerCreateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
class PurchaseCreateForm(forms.ModelForm):
    class Metat:
        model = Purchase
        fields = "__all__"

# Forms for updating models
class IngredientUpdateForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"


class MenuItemsUpdateForm(forms.ModelForm):
    class Meta:
        model = MenuItems
        fields = '__all__'


class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
