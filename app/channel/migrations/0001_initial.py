# Generated by Django 4.0.1 on 2022-01-24 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel', models.CharField(blank=True, max_length=255, null=True, verbose_name='channel')),
                ('seller_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='seller_id')),
                ('customer_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='customer_id')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
