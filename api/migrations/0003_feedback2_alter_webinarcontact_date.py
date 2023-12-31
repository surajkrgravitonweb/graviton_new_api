# Generated by Django 4.2.4 on 2023-11-03 04:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_webinarcontact_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('first_Poor', models.BooleanField(default=False)),
                ('first_Average', models.BooleanField(default=False)),
                ('first_Excellent', models.BooleanField(default=False)),
                ('Second_Poor', models.BooleanField(default=False)),
                ('Second_Average', models.BooleanField(default=False)),
                ('Second_Excellent', models.BooleanField(default=False)),
                ('Third_Poor', models.BooleanField(default=False)),
                ('Third_Average', models.BooleanField(default=False)),
                ('Third_Excellent', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='webinarcontact',
            name='date',
            field=models.CharField(default=datetime.datetime(2023, 11, 3, 10, 17, 4, 432088), max_length=322, null=True),
        ),
    ]
