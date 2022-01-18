# Generated by Django 4.0 on 2022-01-11 17:24

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.CharField(blank=True, max_length=255, verbose_name='age'),
        ),
        migrations.AddField(
            model_name='user',
            name='car_brand',
            field=models.CharField(blank=True, max_length=255, unique=True, verbose_name='car_brand'),
        ),
        migrations.AddField(
            model_name='user',
            name='car_category',
            field=models.CharField(blank=True, max_length=255, unique=True, verbose_name='car_category'),
        ),
        migrations.AddField(
            model_name='user',
            name='car_color',
            field=models.CharField(blank=True, max_length=255, unique=True, verbose_name='car_color'),
        ),
        migrations.AddField(
            model_name='user',
            name='car_price',
            field=models.CharField(blank=True, max_length=255, unique=True, verbose_name='car_price'),
        ),
        migrations.AddField(
            model_name='user',
            name='car_transmission',
            field=models.CharField(blank=True, max_length=255, unique=True, verbose_name='car_transmission'),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, max_length=255, verbose_name='gender'),
        ),
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.CharField(blank=True, max_length=255, unique=True, verbose_name='location'),
        ),
        migrations.AddField(
            model_name='user',
            name='middlename',
            field=models.CharField(blank=True, max_length=255, verbose_name='middlename'),
        ),
        migrations.AddField(
            model_name='user',
            name='occupation',
            field=models.CharField(blank=True, max_length=255, verbose_name='occupation'),
        ),
        migrations.AddField(
            model_name='user',
            name='payslip',
            field=models.ImageField(default='uploads/users_placeholder.png', upload_to=users.models.nameFile, verbose_name='payslip'),
        ),
        migrations.AddField(
            model_name='user',
            name='suffix',
            field=models.CharField(blank=True, max_length=255, verbose_name='suffix'),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=255, verbose_name='username'),
        ),
    ]
