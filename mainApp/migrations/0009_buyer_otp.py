# Generated by Django 4.1.7 on 2023-04-10 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0008_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='otp',
            field=models.IntegerField(default=-1155),
        ),
    ]
