# Generated by Django 5.1.3 on 2024-11-14 23:46

import django_countries.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EcommApp', '0007_chckout_order_orderitem_payment_shippingaddress_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]