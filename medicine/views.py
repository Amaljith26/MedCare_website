from django.shortcuts import render
from .models import MedicineList

# Create your views here.
def Medlist(request):
    return render(request,'medicines.html')

def Productlists(request):
    product_list = MedicineList.objects.all()
    return render(request, 'medicines.html',{'product_list':product_list})