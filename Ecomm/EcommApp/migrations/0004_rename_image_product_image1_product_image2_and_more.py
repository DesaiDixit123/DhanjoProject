# Generated by Django 5.1.3 on 2024-11-12 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcommApp', '0003_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/products'),
        ),
        migrations.AddField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/products'),
        ),
        migrations.AddField(
            model_name='product',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/products'),
        ),
        migrations.AddField(
            model_name='product',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/products'),
        ),
    ]
