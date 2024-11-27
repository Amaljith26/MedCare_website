from django.shortcuts import render,redirect
from . models import Appointment
from django.contrib import messages

# Create your views here.
def Homepage(request):
    return render(request, 'index.html')

def check(request):
    return render(request, 'heartform.html')


def AppointmentInfo(request):

    if request.method == "POST":
        # Fetch data from the form
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        category = request.POST.get('category')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        
        Appointment.objects.create(
            name=name,
            phone=phone,
            category=category,
            email=email,
            message = message,
        )

        # Add a success message
        messages.success(request, f"Thank you {name}, your appointment request has been received!")

        # Render the form again with acknowledgment
        return render(request, 'index.html', {'name': name})

    # Render the default form
    return render(request, 'index.html')
