from django.shortcuts import render, redirect
from .models import WasteType
from django.contrib import messages
from .forms import WasteTypeForm

def waste_type(request):

    if request.method == "POST":
        form = WasteTypeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Waste Type added successfully!")
            return redirect('waste-type')
        else:
            messages.error(request, "Something went wrong!")
            print(form.errors)
            return redirect('waste-type')
        
    waste_types = WasteType.objects.all()
    form = WasteTypeForm()
    context = {
        'waste_types': waste_types,
        'form':form

    }
    return render(request, 'Waste/waste_type.html', context)

def delete_waste_type(request, id):

    waste_type = WasteType.objects.get(id=id)
    waste_type.delete()
    messages.success(request, 'Waste type deleted successfully.')
    return redirect('waste-type')


def edit_waste_type(request, id):

    waste_type = WasteType.objects.get(id=id)

    if request.method == "POST":
        form = WasteTypeForm(request.POST, request.FILES, instance=waste_type)
        if form.is_valid():
            form.save()
            messages.success(request, "Waste type edited successfully!")
            return redirect('waste-type')
        else:
            messages.error(request, "Something went wrong!")
            print(form.errors)
            return redirect('waste-type')
        
    form = WasteTypeForm(instance=waste_type)
    context = {
        'form': form,
        'waste_type': waste_type
    }
    return render(request, 'Waste/edit-waste-type.html', context)

    

