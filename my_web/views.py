from django.shortcuts import render, redirect
from my_web.forms import ContactForm



# Create your views here.
def home(request):
    return render(request, 'my_web/home.html')

def about(request):
    return render(request, 'my_web/about.html')


def projects(request):
    return render(request, 'my_web/projects.html')



# forms view define

def contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            submitted = True
            form = ContactForm()
    else:
        form = ContactForm()
    return render(request, 'my_web/contact.html', {'form': form, 'submitted': submitted})