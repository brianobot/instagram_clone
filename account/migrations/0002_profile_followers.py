# Generated by Django 4.0.2 on 2022-10-03 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='followers',
            field=models.ManyToManyField(to='account.Profile'),
        ),
    ]