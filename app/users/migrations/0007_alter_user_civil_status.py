# Generated by Django 4.0.1 on 2022-01-19 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_user_status_user_civil_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='civil_status',
            field=models.CharField(blank=True, max_length=255, verbose_name='civil_status'),
        ),
    ]
