from django.shortcuts import render, redirect
from .models import FoodWaste
from django.contrib import messages
from .forms import FoodWasteForm

def food_waste(request):
    
    if request.method == "POST":
        form = FoodWasteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Food Waste added successfully!")
            return redirect('food-waste')
        else:
            messages.error(request, "Something went wrong!")
            print(form.errors)
            return redirect('food-waste')
        
    food_wastes = FoodWaste.objects.all()
    form = FoodWasteForm()
    context = {
        'food_wastes': food_wastes,
        'form':form

    }
    return render(request, 'Waste/food-waste.html', context)


def delete_food_waste(request, id):

    food_waste = FoodWaste.objects.get(id=id)
    food_waste.delete()
    messages.success(request, 'Food waste deleted successfully.')
    return redirect('food-waste')

def edit_food_waste(request, id):
    
    food_waste = FoodWaste.objects.get(id=id)

    if request.method == "POST":
        form = FoodWasteForm(request.POST, request.FILES, instance=food_waste)
        if form.is_valid():
            form.save()
            messages.success(request, "Food waste edited successfully!")
            return redirect('food-waste')
        else:
            messages.error(request, "Something went wrong!")
            print(form.errors)
            return redirect('food-waste')
        
    form = FoodWasteForm(instance=food_waste)
    context = {
        'form': form,
        'food_waste': food_waste
    }
    return render(request, 'Waste/edit-food-waste.html', context)   
