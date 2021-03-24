from django.http import request
from django.shortcuts import render
from django.contrib import messages
from .models import ContactModel

# Create your views here.

# Test static files and database
def home(request):
    if request.method == 'POST':
        print(request.POST)
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('subject') and request.POST.get('message'):
            contact = ContactModel()
            contact.name = request.POST.get('name')
            contact.email = request.POST.get('email')
            contact.subject = request.POST.get('subject')
            contact.message = request.POST.get('message')
            contact.save()

            messages.success(request, "Thank you for reaching out to us.")

            return render(request, "core/learn/index.html")

    return render(request, 'core/learn/index.html')
