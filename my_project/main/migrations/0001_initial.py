# Generated by Django 4.2.3 on 2023-07-31 17:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjetecDjango',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('year', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('data', models.DateTimeField(default=datetime.datetime(2023, 7, 31, 14, 50, 14, 683003), verbose_name='Posting date')),
            ],
        ),
    ]
