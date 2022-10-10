from django.shortcuts import render, redirect

# Create your views here.

# Homepage

def homepage(request):
    return render(request, 'homepage/homepage.html')

def in_construction(request):
    return render(request, 'homepage/in_construction.html')