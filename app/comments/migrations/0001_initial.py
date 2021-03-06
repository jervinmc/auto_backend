# Generated by Django 4.0.1 on 2022-01-25 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, max_length=255, null=True, verbose_name='label')),
                ('user_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='user_id')),
                ('customer_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='customer_name')),
                ('listing_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='listing_id')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
