# Generated by Django 4.0.1 on 2022-01-25 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sold', '0002_remove_sold_listing_id_sold_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sold',
            name='user_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='user_id'),
        ),
    ]
