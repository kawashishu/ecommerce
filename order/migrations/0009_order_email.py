# Generated by Django 4.1.2 on 2022-11-10 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_order_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.CharField(default=2, max_length=200, unique=True),
            preserve_default=False,
        ),
    ]
