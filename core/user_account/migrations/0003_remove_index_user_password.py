# Generated by Django 4.1.1 on 2022-09-27 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0002_alter_index_user_creation_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='index_user',
            name='password',
        ),
    ]