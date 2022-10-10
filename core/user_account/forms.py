from socket import fromshare
from django import forms

from .models import Index_user

class IndexUserForm(forms.ModelForm):

    firstname = forms.CharField(label='Firstname', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    lastname = forms.CharField(label='Lastname', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={
        'class': 'form-control'
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

    class Meta:
        model = Index_user
        fields = '__all__' #si juste '__all__', on prend tous les champs du models