# Generated by Django 4.2.3 on 2023-07-31 21:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_my_movies_date_alter_my_movies_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='my_movies',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 31, 18, 17, 54, 379130), verbose_name='Posting date'),
        ),
    ]
