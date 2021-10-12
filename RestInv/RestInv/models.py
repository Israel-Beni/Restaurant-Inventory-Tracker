from django.db import models
import datetime

# Ingredient Model
class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0, blank=False)
    description = models.TextField(default='')
    available_quantity = models.IntegerField(default=0, blank=False)
    GRAMME = 'gr'
    POUNDS = 'pd'
    OUNCE = 'ow'
    unit_choices = [
        (GRAMME, 'Grammes'),
        (POUNDS, 'Pounds'),
        (OUNCE, 'Ounce'),
    ]
    quantity_unit = models.CharField(default='grams', choices=unit_choices)

# MenuItem Model
class MenuItems(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    price = models.IntegerField(default=0)
    recipe_requirement = []

# Customer Model
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    name = f"{first_name} {middle_name} {last_name}"

# Purchase Model
class Purchase(models.Model):
    purchase_datetime = 0
    total = 0
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    tax = 0
