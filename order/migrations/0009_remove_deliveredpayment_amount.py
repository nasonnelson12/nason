# Generated by Django 3.1.2 on 2020-12-30 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_deliveredpayment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliveredpayment',
            name='amount',
        ),
    ]
