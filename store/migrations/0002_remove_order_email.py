# Generated by Django 4.1.2 on 2022-11-30 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='email',
        ),
    ]
