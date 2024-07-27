from .models import Problem
from django import forms

class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['name', 'description', 'image', 'seriousness', 'problem_type']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'seriousness': forms.Select(attrs={'class': 'form-control'}),
            'problem_type': forms.Select(attrs={'class': 'form-control'}),
        }