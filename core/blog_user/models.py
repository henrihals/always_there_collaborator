from django.db import models

# Create your models here.

class Index_blog_user(models.Model):

    id_blog = models.AutoField(primary_key=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, null=False)
    content_blog = models.TextField(null=False)

    def __str__(self):
        return f'{self.id_blog}   /   {self.creation_date}  /   {self.title}'