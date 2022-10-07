from socket import fromshare
from django import forms

from .models import Index_collaborator

class IndexCollaboratorForm(forms.ModelForm):
    class Meta:
        model = Index_collaborator
        fields = {'firstname', 'lastname', 'email', 'street', 'number_street', 'zip_code', 'town', 'country', 'prefix_gsm', 'gsm'} #si juste '__all__', on prend tous les champs du models