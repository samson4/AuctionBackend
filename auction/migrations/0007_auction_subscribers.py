# Generated by Django 4.2.3 on 2023-08-16 11:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auction', '0006_remove_auction_subscribed'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='subscribers',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
