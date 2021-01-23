# Generated by Django 3.1.2 on 2021-01-02 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_remove_deliveredpayment_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='district',
            field=models.CharField(choices=[('Ilemela', 'Ilemela'), ('Nyamagana', 'Nyamagana'), ('Misungwi', 'Misungwi'), ('Magu', 'Magu')], default='Nyamagana', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='region',
            field=models.CharField(choices=[('Mwanza', 'Mwanza')], default='Mwanza', max_length=100),
        ),
    ]