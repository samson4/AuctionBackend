# Generated by Django 4.2.3 on 2023-08-21 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0009_alter_auction_subscribers'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'Active'), ('PREPARING', 'PREPARING')], default='PREPARING', max_length=50),
        ),
    ]
