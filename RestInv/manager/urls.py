from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ingredients/', views.IngredientList.as_view(), name='ingredients'),
    path('menu_items/', views.MenuItemsList.as_view(), name='menu_items'),
    path('customers/', views.CustomerList.as_view(), name='customers'),
    path('purchases/', views.PurchaseList.as_view(), name='purchases'),
    path('ingredient/create/', views.IngredientCreate.as_view(), name='create_ingredient'),
    path('menu_item/create/', views.MenuItemsCreate.as_view(), name='create_menu_item'),
    path('customer/create/', views.CustomerCreate.as_view(), name='create_customer'),
]