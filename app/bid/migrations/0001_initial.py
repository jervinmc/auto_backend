# Generated by Django 4.0.1 on 2022-01-26 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='user_id')),
                ('customer_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='customer_id')),
                ('listing_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='listing_id')),
                ('customer_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='customer_name')),
                ('image', models.CharField(blank=True, max_length=255, null=True, verbose_name='image')),
                ('bid_price', models.CharField(blank=True, max_length=255, null=True, verbose_name='bid_price')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]