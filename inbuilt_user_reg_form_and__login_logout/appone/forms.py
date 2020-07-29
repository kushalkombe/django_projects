from django import forms
# #from django.contrib.auth.forms import UserCreationForm
#
# class UserRegistrationForm(UserCreationForm):
#     class Meta:
#         model=User
#         fields='__all__'
from appone.models import ImageModel
class ImageModelForm(forms.ModelForm):
    class Meta:
        model=ImageModel
        fields='__all__'
