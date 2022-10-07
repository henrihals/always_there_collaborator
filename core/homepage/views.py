from django.shortcuts import render, redirect

# Create your views here.

# Homepage

def homepage(request):
    return render(request, 'homepage/homepage.html')