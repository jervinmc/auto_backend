# Generated by Django 4.0.1 on 2022-01-25 20:32

from django.db import migrations, models
import sold.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sold',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='customer_name')),
                ('customer_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='customer_id')),
                ('listing_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='listing_id')),
                ('car_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='car_name')),
                ('image', models.ImageField(default='uploads/users_placeholder.png', upload_to=sold.models.nameFile, verbose_name='image')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
