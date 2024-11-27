from django.shortcuts import render,redirect
from django.shortcuts import render
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
from django.conf import settings
from .models import HeartData,BmiIndex


# Load the trained model and scaler from disk
model_path = 'service/new_data/train_model.pkl'
scaler_path = 'service/new_data/scaler.pkl'

def load_model_and_scaler():
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)
    with open(scaler_path, 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)
    return model, scaler

def check(request):
    return render(request,'heartform.html')

def predict(request):
    prediction = None
    if request.method == 'POST':
        # Collect data from the form
        features = [
            float(request.POST['age']),
            int(request.POST['sex']),
            int(request.POST['cp']),
            int(request.POST['trestbps']),
            int(request.POST['chol']),
            int(request.POST['fbsr']),
            int(request.POST['restecg']),
            int(request.POST['thalach']),
            int(request.POST['exang']),
            float(request.POST['oldpeak']),
            int(request.POST['slope']),
            int(request.POST['ca']),
            int(request.POST['thal']),
        ]
        
        HeartData.objects.create(
                age=features[0],
                sex=features[1],
                cp=features[2],
                trestbps=features[3],
                chol=features[4],
                fbsr=features[5],
                restecg=features[6],
                thalach=features[7],
                exang=features[8],
                oldpeak=features[9],
                slope=features[10],
                ca=features[11],
                thal=features[12],

            )
        
        # Load the model and scaler
        model, scaler = load_model_and_scaler()

        # Scale the features
        features_scaled = scaler.transform([features])

        # Make prediction
        prediction_result = model.predict(features_scaled)


        prediction = "Consult a Doctor: Heart Disease Likely" if prediction_result == 1 else "No chance of Heart Disease"

    return render(request, 'heartform.html', {
    'prediction': prediction,
    'prediction_result': prediction_result,
})

# Create your views here.
from django.shortcuts import render
from .models import BmiIndex

from django.shortcuts import render

def bmicheck(request):
    bmi = None
    bmi_category = None
    name = None
    age = None
    height = None
    weight = None

    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        height = request.POST.get('height') 
        weight = request.POST.get('weight')

        if height and weight:
            try:
                # Convert height and weight to float for calculation
                height = float(height)
                weight = float(weight)

                # Calculate BMI
                bmi = weight / (height / 100) ** 2  

                # Categorize BMI
                if bmi < 18.5:
                    bmi_category = 'Underweight'
                elif 18.5 <= bmi <= 24.9:
                    bmi_category = 'Normal Weight'
                elif 25 <= bmi <= 29.9:
                    bmi_category = 'Overweight'
                elif 30 <= bmi <= 39.9:
                    bmi_category = 'Obesity'
                else:
                    bmi_category = 'Severe Obesity'

                BmiIndex.objects.create(
                    name=name,
                    age=age,
                    height=height,
                    weight=weight,
                    bmi=bmi,
                    bmi_category=bmi_category
                )

            except ValueError:
                error_message = "Please enter valid numeric values for height and weight."
                return render(request, 'bmiform.html', {'error_message': error_message})

        else:
            error_message = "Both height and weight are required."
            return render(request, 'bmiform.html', {'error_message': error_message})

    context = {
        'name': name,
        'age': age,
        'height': height,
        'weight': weight,
        'bmi': bmi,
        'bmi_category': bmi_category,
        'result': f"Your BMI is: {bmi:.2f}" if bmi else None,
    }

    return render(request, 'bmiform.html', context)


