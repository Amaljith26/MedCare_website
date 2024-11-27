import os
import pandas as pd
from django.core.management.base import BaseCommand
from django.apps import apps
from doctors.models import Doctor

class Command(BaseCommand):
    help = 'Load doctor data from a CSV file'

    def handle(self, *args, **kwargs):
        # Dynamically get the file path
        app_config = apps.get_app_config('doctors')
        file_path = os.path.join(app_config.path, 'datas', 'doctor_data.csv')

        # Load the data using pandas
        data = pd.read_csv(file_path)

        # Populate the database
        for _, row in data.iterrows():
            Doctor.objects.create(
                name=row['name'],
                specialization=row['specialization'],
                address=row['address'],
                latitude=row['latitude'],
                longitude=row['longitude'],
                contact=row['contact']
            )
        self.stdout.write(self.style.SUCCESS('Successfully loaded doctor data!'))
