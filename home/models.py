from django.db import models


class Appointment(models.Model):

    CATEGORY_CHOICES = [
        ('Orthopedics', 'Orthopedics'),
        ('General Medicine', 'General Medicine'),
        ('Ophthalmologist', 'Ophthalmologist'),
        ('Skin Care', 'Skin Care'),
    ]

    name = models.CharField(default='unknown', max_length =20, null=False, blank=False) 
    phone = models.IntegerField()
    category = models.CharField(
        max_length= 50, 
        choices=CATEGORY_CHOICES, 
        default='General Medicine'
    )
    email = models.EmailField(max_length=255, null=False, blank=False)
    message =models.TextField(default="No message")

    def __str__(self):
        return self.name
    
