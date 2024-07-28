from .models import Problem
from django import forms
from .models import BedsInventory, Ambulance, StaffMember, O2Inventory

class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['name', 'description', 'image', 'seriousness', 'problem_type']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'seriousness': forms.Select(attrs={'class': 'form-control'}),
            'problem_type': forms.Select(attrs={'class': 'form-control'}),
        }

class BedsInventoryForm(forms.ModelForm):
    class Meta:
        model = BedsInventory
        fields = '__all__' 

class AmbulanceForm(forms.ModelForm):
    class Meta:
        model = Ambulance
        fields = '__all__'

class StaffMemberForm(forms.ModelForm):
    class Meta:
        model = StaffMember
        fields = '__all__'

class O2InventoryForm(forms.ModelForm):
    class Meta:
        model = O2Inventory
        fields = '__all__'
