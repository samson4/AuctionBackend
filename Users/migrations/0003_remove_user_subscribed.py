# Generated by Django 4.2.3 on 2023-08-16 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_user_subscribed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='subscribed',
        ),
    ]