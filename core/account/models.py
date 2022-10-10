from distutils.command.upload import upload
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):

    username = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    id_collaborator = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    birthday = models.DateField()
    email = models.EmailField(null=True)
    street = models.CharField(max_length=100, null=True)
    number_street = models.CharField(max_length=10, null=True)
    zip_code = models.CharField(max_length=10, null=True)
    town = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    prefix_gsm = models.PositiveIntegerField(null=True)
    gsm = models.PositiveIntegerField(null=True)
    image = models.ImageField(upload_to="img/img_profile", null=True, blank=True)

    def __str__(self):
        return f'{self.id_collaborator}   /   {self.firstname}   /   {self.lastname}   /   {self.username.username}   /   {self.town}   /   {self.country}  / {self.prefix_gsm}{self.gsm}'
    

