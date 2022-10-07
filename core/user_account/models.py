from django.db import models

# Create your models here.

# DB data collaborator

class Index_user(models.Model):

    id_user = models.AutoField(primary_key=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    firstname = models.CharField(max_length=50, null=False)
    lastname = models.CharField(max_length=50, null=False)
    #password = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=100, unique=True, null=False)
    street = models.CharField(max_length=100, null=False)
    number_street = models.CharField(max_length=10, null=False)
    zip_code = models.CharField(max_length=10, null=False)
    town = models.CharField(max_length=50, null=False)
    country = models.CharField(max_length=50, null=False)
    prefix_gsm = models.PositiveIntegerField(null=False)
    gsm = models.PositiveIntegerField(null=False)

    def __str__(self):
        return f'{self.id_user}   /   {self.creation_date}   /   {self.firstname}   /   {self.lastname}   /   {self.email}   /   {self.town}   /   {self.country}  / {self.prefix_gsm}{self.gsm}'

class Join_table_user(models.Model):

    id_user = models.ForeignKey(to=Index_user, on_delete=models.CASCADE)
    #id_blog = models.ForeignKey(to=Index_blog, on_delete=models.CASCADE, blank="")

    def __str__(self):
        return f'{self.id_user}'