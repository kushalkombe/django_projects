from django import forms

class NameForm(forms.Form):
    name=forms.CharField(max_length=20)

class AgeForm(forms.Form):
    age=forms.IntegerField()

class GFNameForm(forms.Form):
    gfname=forms.CharField(max_length=20)
