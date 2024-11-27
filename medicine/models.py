from django.db import models

# Create your models here.
class MedicineList(models.Model):
    name = models.CharField(max_length=10, default='Required')
    price = models.FloatField()
    image= models.ImageField(upload_to='products/image', default="")


    def __str__(self):
        return self.name
