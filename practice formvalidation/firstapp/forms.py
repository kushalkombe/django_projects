from django import forms
from django.core import validators


class FeedbackForm(forms.Form):
    rollno = forms.IntegerField()
    name = forms.CharField()
    email = forms.EmailField()
    marks = forms.FloatField()
    feedback = forms.CharField(widget=forms.Textarea, validators=[
                               validators.MinLengthValidator(10)])
    # def clean_rollno(self):
    #     print('validating rollno')
    #     frollno = self.cleaned_data['rollno']
    #     return frollno

    # def clean_name(self):
    #     print('validating name')
    #     fname = self.cleaned_data['name']
    #     if len(fname) < 4:
    #         raise forms.ValidationError(
    #             'The minimum no of charactor in the name field should be 4')
    #     return fname

    # def clean_email(self):
    #     print('validating email')
    #     femail = self.cleaned_data['email']
    #     if 'edu' in femail:
    #         raise forms.ValidationError(
    #             'The educationally email is not support')
    #     return femail

    # def clean_marks(self):
    #     print('validating marks')
    #     fmarks = self.cleaned_data['marks']
    #     if fmarks >= 100:
    #         raise forms.ValidationError('Marks should be less then 100')
    #     return fmarks

    def clean(self):
        print('Total form validation...')
        total_cleaned_data = super().clean()

        frollno = total_cleaned_data['rollno']
        if frollno <= 0:
            raise forms.ValidationError('Rollno should be > 0')

        fname = total_cleaned_data['name']
        if len(fname) < 4:
            raise forms.ValidationError(
                'The minimum no of charactor in the name field should be 4')

        femail = self.cleaned_data['email']
        if 'edu' in femail:
            raise forms.ValidationError(
                'The educationally email is not support')

        fmarks = self.cleaned_data['marks']
        if fmarks > 100:
            raise forms.ValidationError('Marks should be less then 100')
