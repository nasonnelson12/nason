# Generated by Django 3.1.2 on 2020-11-13 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_order_orderproduct'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='amount',
        ),
    ]
