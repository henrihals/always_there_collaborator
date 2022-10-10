from tkinter import Widget
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Profile

# Creation username and password

class UserForm(UserCreationForm):

    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))
    password2 = forms.CharField(label='Confirm your password', widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

# Creation data personal user

class ProfileForm(forms.ModelForm):

    firstname = forms.CharField(label='Firstname', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    lastname = forms.CharField(label='Lastname', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={
        'class': 'form-control'
    }))
    birthday = forms.DateField(label='Birthday', widget=forms.DateInput(attrs={
        'class': 'form-control',
        'type': 'date'
    }))
    street = forms.CharField(label='Street', widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    number_street = forms.IntegerField(label='Number street', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'number'
    }))
    zip_code = forms.IntegerField(label='Zip-number', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'number'
    }))
    town = forms.CharField(label='Town', widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    country = forms.CharField(label='Country', widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    prefix_gsm = forms.IntegerField(label='Prefix GSM', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'number'
    }))
    gsm = forms.IntegerField(label='Number GSM', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'number'
    }))
    # image = forms.ImageField(label="Photo" (attrs={
    #     'class': 'form-image',
    # }))
    
    class Meta:
        model = Profile
        fields = ('firstname', 'lastname', 'email', 'birthday', 'street', 'number_street', 'zip_code', 'town', 'country', 'prefix_gsm', 'gsm', 'image')

# update username

# class ChangeUserForm(UserChangeForm):

#     id_username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
#         'class': 'form-control'
#     }))

#     class Meta:
#         model = User
#         fields = ('id_username',)