# Generated by Django 4.1.2 on 2022-11-06 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='billingaddress',
            old_name='user',
            new_name='email',
        ),
    ]
