# Generated by Django 4.1.2 on 2022-11-17 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_customer_avatar_alter_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customer',
            name='sex',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('U', 'Unsure')], default='U', max_length=1),
        ),
    ]
