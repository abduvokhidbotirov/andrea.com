from django.shortcuts import render
from .forms import ContactForm
from .models import *


# Create your views here.


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContactForm()

    email = request.GET.get('email')
    if email:
        Subscribe.objects.create(email=email)
    ctx = {
        'form': form
    }
    return render(request, 'contact.html', ctx)


def about(request):
    email = request.GET.get('email')
    if email:
        Subscribe.objects.create(email=email)
    return render(request, 'about.html')