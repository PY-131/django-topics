# Generated by Django 4.0.1 on 2022-06-15 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]