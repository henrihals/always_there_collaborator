# Generated by Django 4.1.1 on 2022-09-24 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index_user',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]