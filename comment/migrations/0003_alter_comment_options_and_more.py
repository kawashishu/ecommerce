# Generated by Django 4.1.3 on 2023-01-16 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='customerid',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='productid',
            new_name='product',
        ),
    ]