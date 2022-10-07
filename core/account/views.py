from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm

# Create your views here.

# create account collaborator

def register_account_collaborator(request):

    if request.user.is_authenticated:
        return redirect('homepage')
    if request.method ==  "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register-collaborator')
        
    else:
        form = UserForm()

    return render(request, "account/register_account_collaborator.html", { 'form' : form })

# create account user

def register_account_user(request):

    if request.user.is_authenticated:
        return redirect('homepage')
    if request.method ==  "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register-user')
        
    else:
        form = UserForm()

    return render(request, "account/register_account_user.html", { 'form' : form })