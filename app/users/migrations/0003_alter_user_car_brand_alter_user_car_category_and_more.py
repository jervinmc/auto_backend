# Generated by Django 4.0 on 2022-01-11 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_age_user_car_brand_user_car_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='car_brand',
            field=models.CharField(blank=True, max_length=255, verbose_name='car_brand'),
        ),
        migrations.AlterField(
            model_name='user',
            name='car_category',
            field=models.CharField(blank=True, max_length=255, verbose_name='car_category'),
        ),
        migrations.AlterField(
            model_name='user',
            name='car_color',
            field=models.CharField(blank=True, max_length=255, verbose_name='car_color'),
        ),
        migrations.AlterField(
            model_name='user',
            name='car_price',
            field=models.CharField(blank=True, max_length=255, verbose_name='car_price'),
        ),
        migrations.AlterField(
            model_name='user',
            name='car_transmission',
            field=models.CharField(blank=True, max_length=255, verbose_name='car_transmission'),
        ),
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.CharField(blank=True, max_length=255, verbose_name='location'),
        ),
    ]
