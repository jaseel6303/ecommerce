# Generated by Django 4.2.2 on 2023-06-21 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_payment_orderplaced'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderplaced',
            old_name='Customer',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='orderplaced',
            old_name='Product',
            new_name='product',
        ),
    ]
