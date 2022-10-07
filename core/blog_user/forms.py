from socket import fromshare
from django import forms

from .models import Index_blog_user

class IndexBlogUserForm(forms.ModelForm):
    class Meta:
        model = Index_blog_user
        fields = {'title', 'content_blog'} #si juste '__all__', on prend tous les champs du models