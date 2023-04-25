from django.shortcuts import render
from .forms import PatientForm
from .models import Patient
from application.predict import get_prediction
from application.generateCSV import generer_csv
# Create your views here.


def index(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            nom = request.POST['nom']
            prenom = request.POST['prenom']
            sexe = request.POST['sexe']
            age = request.POST['age']
            poids = request.POST['poids']
            taille = request.POST['taille']
            salivation = request.POST['salivation']
            cutting = request.POST['cutting']
            turning_in_bed = request.POST['turning_in_bed']
            alsfrs = request.POST['alsfrs']
            symptom_duration = request.POST['symptom_duration']
            pulse = request.POST['pulse']
            systolic_blood_pressure = request.POST['systolic_blood_pressure']

            result = get_prediction(int(sexe), int(age), float(poids), float(taille), int(salivation), int(cutting), int(turning_in_bed),
                                    int(alsfrs), float(symptom_duration), float(pulse), float(systolic_blood_pressure))

            mort = result[0]
            survie = result[1]
            prediction = result[2]

            patient = Patient(
                nom=nom,
                prenom=prenom,
                sexe=sexe,
                age=age,
                poids=poids,
                taille=taille,
                salivation=salivation,
                cutting=cutting,
                turning_in_bed=turning_in_bed,
                alsfrs=alsfrs,
                symptom_duration=symptom_duration,
                pulse=pulse,
                systolic_blood_pressure=systolic_blood_pressure,
                prediction=prediction,
                vivant=survie,
                mort=mort,
            )

            patient.save()

            return render(request, "prediction.html", {
                'nom': nom,
                'prenom': prenom,
                'mort':  round(mort * 100, 2),
                'survie': round(survie*100, 2),
                'prediction': prediction,

            })

    else:
        form = PatientForm()

    return render(request, "index.html", {'form': form})


def prediction(request):
    nom = request.GET.get('nom')
    prenom = request.GET.get('prenom')
    mort = request.GET.get('mort')
    survie = request.GET.get('survie')
    prediction = request.GET.get('prediction')

    return render(request, "prediction.html", {
        'nom': nom,
        'prenom': prenom,
        'mort': mort,
        'survie': survie,
        'prediction': prediction,
    })


2
