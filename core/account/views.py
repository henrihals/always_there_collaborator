from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm, ProfileForm

# Create your views here.

# create account collaborator

def register_account_collaborator(request):

    if request.user.is_authenticated:
        return redirect('homepage')
    
    form = UserForm(request.POST or None)
    profile_form = ProfileForm(request.POST or None)

    if request.method ==  "POST":
        form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        if form.is_valid() and profile_form.is_valid():
            username = form.save(commit=False)
            profile = profile_form.save(commit=False)
            profile.username = username
            username.save()
            profile.save()
            return redirect('login')

    return render(request, "account/register_account.html", { 'form' : form, 'profile': profile_form })