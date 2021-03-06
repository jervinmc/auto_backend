# Generated by Django 4.0.1 on 2022-02-02 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_user_signed_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='city_of',
            field=models.CharField(blank=True, max_length=255, verbose_name='city_of'),
        ),
        migrations.AddField(
            model_name='user',
            name='mailing_address',
            field=models.CharField(blank=True, max_length=255, verbose_name='mailing_address'),
        ),
        migrations.AddField(
            model_name='user',
            name='state_of',
            field=models.CharField(blank=True, max_length=255, verbose_name='state_of'),
        ),
    ]
