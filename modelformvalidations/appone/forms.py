from django import forms

class StudentForm(forms.Form):
    name=forms.CharField()
    marks = forms.IntegerField()
    email = forms.EmailField()
    address=forms.CharField()


    def clean_name(self):
        name=self.cleaned_data['name']
        if len(name)<=4:
            raise forms.ValidationError('this is invalid name please length on name must be greater than 4')
        return name

    def clean_marks(self):
        marks=self.cleaned_data['marks']
        if marks >=100:
            raise forms.ValidationError('please enter marks less than 100')
        return marks

    def clean_email(self):
        email=self.cleaned_data['email']
        if '.edu' in email:
            raise forms.ValidationError('sorry we do not accept the educational email')
        return email

    def clean_address(self):
        l = ['ahmadnagar','nagpur','pune','mumbai', 'chandrapur','yavatmal','wardha']
        address=self.cleaned_data['address']
        if address not in l:
            raise forms.ValidationError('please fill the whole address')
        return address
