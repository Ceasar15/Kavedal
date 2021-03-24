from django.http import request
from django.shortcuts import render
from .models import ContactModel

# Create your views here.

# Test static files and database
def home(request):
    if request.method == 'POST':
        print(request.POST)
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('subject') and request.POST.get('message'):
            contact = ContactModel()
            contact.fullname = request.POST.get('fullname')
            contact.email = request.POST.get('email')
            contact.phone = request.POST.get('phone')
            contact.subject = request.POST.get('subject')
            contact.save()

    return render(request, 'core/learn/index.html')
