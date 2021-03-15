from django.http import request
from django.shortcuts import render

# Create your views here.

# Test static files and database
def home(request):
    return render(request, 'core/home.html')
