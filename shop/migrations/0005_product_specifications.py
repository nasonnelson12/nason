# Generated by Django 3.1.2 on 2020-10-30 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20201026_0337'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='specifications',
            field=models.TextField(blank=True, null=True),
        ),
    ]
