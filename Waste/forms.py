from django import forms
from .models import Student, WasteType, FoodWaste

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'roll', 'image')
        ## adding bootstrap form control class in each fields
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'roll': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

class WasteTypeForm(forms.ModelForm):
    class Meta:
        model = WasteType
        fields = ('name', 'description', 'image')

class FoodWasteForm(forms.ModelForm):
    class Meta:
        model = FoodWaste
        fields = ('name', 'type', 'description', 'source', 'where_to_throw', 'image', 'time_to_decay', 'carbon_footprint', 'added_by')

