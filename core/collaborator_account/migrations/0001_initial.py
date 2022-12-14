# Generated by Django 4.1.1 on 2022-09-21 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Index_collaborator',
            fields=[
                ('id_collaborator', models.AutoField(primary_key=True, serialize=False)),
                ('creation_date', models.DateTimeField()),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('street', models.CharField(max_length=100)),
                ('number_street', models.CharField(max_length=10)),
                ('zip_code', models.CharField(max_length=10)),
                ('town', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('prefix_gsm', models.PositiveIntegerField()),
                ('gsm', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Join_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_collaborator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collaborator_account.index_collaborator')),
            ],
        ),
    ]
