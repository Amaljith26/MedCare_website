# Generated by Django 5.1.3 on 2024-11-23 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_bmiindex'),
    ]

    operations = [
        migrations.AddField(
            model_name='bmiindex',
            name='bmi_category',
            field=models.CharField(default='Unknown', max_length=50),
        ),
    ]
