from django.contrib import admin
from .models import HeartData,BmiIndex

@admin.register(HeartData)
class HeartDataAdmin(admin.ModelAdmin):
    list_display = ('age', 'sex', 'cp', 'trestbps', 'chol','fbsr' ,'restecg','thalach','exang','oldpeak','slope','ca','thal') 

# Register your models here.
@admin.register(BmiIndex)
class BmiIndexAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'height', 'weight', 'bmi','bmi_category')
