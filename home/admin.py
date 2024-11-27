from django.contrib import admin
from . models import Appointment
# Register your models here.

@admin.register(Appointment)
class AppointmentInfos(admin.ModelAdmin):
    list_display = ('name','phone','category','email','message')