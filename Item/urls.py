from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"), 
    path('food-waste', views.food_waste_list, name="food_waste_list"),
    path('food-waste/<int:food_waste_id>', views.food_waste_detail, name="food_waste_detail"),
    path('data-model', views.data_model, name="data_model"),
    
]