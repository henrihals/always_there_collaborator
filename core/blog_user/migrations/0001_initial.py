# Generated by Django 4.1.1 on 2022-09-21 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Index_blog_user',
            fields=[
                ('id_blog', models.AutoField(primary_key=True, serialize=False)),
                ('creation_date', models.DateTimeField()),
                ('title', models.CharField(max_length=100)),
                ('content_blog', models.TextField()),
            ],
        ),
    ]
