# Generated by Django 4.2.4 on 2023-11-01 05:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebinarContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='null', max_length=200, null=True)),
                ('LastName', models.CharField(default='null', max_length=200, null=True)),
                ('email', models.CharField(default='null', max_length=200, null=True)),
                ('phone', models.IntegerField(default='null', max_length=12, null=True)),
                ('message', models.CharField(default='null', max_length=200, null=True)),
                ('date', models.CharField(default=datetime.datetime(2023, 11, 1, 11, 15, 35, 660868), max_length=322, null=True)),
            ],
        ),
    ]
