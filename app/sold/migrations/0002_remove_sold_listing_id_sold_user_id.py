# Generated by Django 4.0.1 on 2022-01-25 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sold', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sold',
            name='listing_id',
        ),
        migrations.AddField(
            model_name='sold',
            name='user_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='listing_id'),
        ),
    ]
