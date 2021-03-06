# Generated by Django 4.0 on 2022-01-18 12:11

import activity.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='title')),
                ('user_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='user_id')),
                ('image', models.ImageField(default='uploads/users_placeholder.png', upload_to=activity.models.nameFile, verbose_name='image')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
