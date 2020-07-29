from django import forms
from aoo1.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name','marks']
