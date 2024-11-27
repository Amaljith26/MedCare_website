from django.shortcuts import render
from .models import Doctor
from django.db.models import Q

def doctor_list(request):
    # Use GET instead of POST for query retrieval
    query = request.GET.get('q', '')
    
    # Filter doctors based on search query or return all doctors
    doctors = Doctor.objects.filter(
        Q(name__icontains=query) |
        Q(specialization__icontains=query) |
        Q(address__icontains=query)
    ) if query else Doctor.objects.all()
    
    # Render the template with context
    return render(request, 'doctor.html', {'doctors': doctors, 'query': query})
