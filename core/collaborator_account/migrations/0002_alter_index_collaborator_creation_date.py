# Generated by Django 4.1.1 on 2022-09-24 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collaborator_account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index_collaborator',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
