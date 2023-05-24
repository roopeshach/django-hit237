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
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

class FoodWasteForm(forms.ModelForm):
    class Meta:
        model = FoodWaste
        fields = ('name', 'type', 'description', 'source', 'where_to_throw', 'image', 'time_to_decay', 'carbon_footprint', 'added_by')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'source': forms.TextInput(attrs={'class': 'form-control'}),
            'where_to_throw': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'time_to_decay': forms.TextInput(attrs={'class': 'form-control'}),
            'carbon_footprint': forms.TextInput(attrs={'class': 'form-control'}),
            'added_by': forms.Select(attrs={'class': 'form-control'}),
        }