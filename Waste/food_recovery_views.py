from django.shortcuts import render, redirect
from .models import FoodRecovery
from django.contrib import messages
from .forms import FoodRecoveryForm

def food_recovery(request):

    if request.method == "POST":
        form = FoodRecoveryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Food Recovery added successfully!")
            return redirect('food-recovery')
        else:
            messages.error(request, "Something went wrong!")
            print(form.errors)
            return redirect('food-recovery')
        
    food_recoveries = FoodRecovery.objects.all()
    form = FoodRecoveryForm()
    context = {
        'food_recoveries': food_recoveries,
        'form':form

    }
    return render(request, 'Waste/food-recovery.html', context)


def delete_food_recovery(request, id):
    
    food_recovery = FoodRecovery.objects.get(id=id)
    food_recovery.delete()
    messages.success(request, 'Food recovery deleted successfully.')
    return redirect('food-recovery')


def edit_food_recovery(request, id):
        
    food_recovery = FoodRecovery.objects.get(id=id)

    if request.method == "POST":
        form = FoodRecoveryForm(request.POST, request.FILES, instance=food_recovery)
        if form.is_valid():
            form.save()
            messages.success(request, "Food recovery edited successfully!")
            return redirect('food-recovery')
        else:
            messages.error(request, "Something went wrong!")
            print(form.errors)
            return redirect('food-recovery')
        
    form = FoodRecoveryForm(instance=food_recovery)
    context = {
        'form': form,
        'food_recovery': food_recovery
    }
    return render(request, 'Waste/edit-food-recovery.html', context)
