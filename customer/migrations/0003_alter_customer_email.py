# Generated by Django 4.1.2 on 2022-10-25 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_customer_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
