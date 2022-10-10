# Generated by Django 4.1.1 on 2022-09-28 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_rename_user_profile_username_remove_profile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='firstname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='lastname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gsm',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='number_street',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='prefix_gsm',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='street',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='town',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='zip_code',
            field=models.CharField(max_length=10, null=True),
        ),
    ]