# Generated by Django 5.1.3 on 2024-11-23 18:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_bmiindex_bmi_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='bmiindex',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]