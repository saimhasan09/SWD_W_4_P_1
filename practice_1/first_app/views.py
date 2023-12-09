from django.shortcuts import render
from . forms import ExampleForm

# Create your views here.

def home(request):
    return render(request, 'home.html')


# function for example form
def django_form(request):
    form = ExampleForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, 'home.html', {'form': form})