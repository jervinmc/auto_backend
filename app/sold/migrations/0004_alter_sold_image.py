# Generated by Django 4.0.1 on 2022-01-25 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sold', '0003_alter_sold_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sold',
            name='image',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
