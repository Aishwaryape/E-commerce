# Generated by Django 3.2.6 on 2021-08-05 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(blank=True, default=0, max_length=50),
        ),
    ]
