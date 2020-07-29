from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from first.models import ImageModel

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class ImageModelForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = '__all__'
