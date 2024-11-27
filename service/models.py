from django.db import models
import datetime

# Create your models here.

class HeartData(models.Model):
    age = models.FloatField()
    sex = models.IntegerField()
    cp = models.IntegerField()
    trestbps = models.IntegerField()
    chol = models.IntegerField()
    fbsr = models.IntegerField()
    restecg = models.IntegerField()
    thalach = models.IntegerField()
    exang = models.IntegerField()
    oldpeak = models.FloatField()
    slope = models.IntegerField()
    ca = models.IntegerField()
    thal = models.IntegerField()

    def __str__(self):
        return f"HeartData Record (Age: {self.age}, Sex: {self.sex})"

from django.db import models

class BmiIndex(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, default="Unknown")
    age = models.IntegerField()  # Ensure this is provided
    height = models.FloatField()
    weight = models.FloatField()
    bmi = models.FloatField()
    bmi_category = models.CharField(max_length=50, default="Unknown")
    date_created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.name} - BMI: {self.bmi:.2f}"
