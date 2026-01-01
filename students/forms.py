from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'course', 'email', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter student name'}),
            'course': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Course'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
        }
