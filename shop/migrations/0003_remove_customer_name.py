# Generated by Django 4.1.6 on 2023-02-09 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_customer_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='name',
        ),
    ]
