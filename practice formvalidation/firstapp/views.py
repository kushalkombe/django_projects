from django.shortcuts import render
from firstapp.forms import FeedbackForm

# Create your views here.


def feedback(request):
    form = FeedbackForm()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print('Validation of form is Successfully')
            print('Rollno :', form.cleaned_data['rollno'])
            print('Name :', form.cleaned_data['name'])
            print('Email :', form.cleaned_data['email'])
            print('Marks :', form.cleaned_data['marks'])
            print('Feedback :', form.cleaned_data['feedback'])
    return render(request, 'index.html', {'form': form})
