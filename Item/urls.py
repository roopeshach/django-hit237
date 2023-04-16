from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"), 
    path('items', views.item_list, name="item_list"),
    path('items/<int:item_id>', views.item_detail, name="item_detail"),
    path('data-model', views.data_model, name="data_model"),
    
]