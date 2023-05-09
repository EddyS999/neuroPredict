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
            sexe = int(request.POST['sexe'])
            age = int(request.POST['age'])
            poids = float(request.POST['poids'])
            taille = float(request.POST['taille'])

            speech = int(request.POST['speech'])
            salivation = int(request.POST['salivation'])

            swallowing = int(request.POST['swallowing'])
            handwriting = int(request.POST['handwriting'])
            cutting = int(request.POST['cutting'])
            dressing = int(request.POST['dressing'])
            turning_in_bed = int(request.POST['turning_in_bed'])

            walking = int(request.POST['walking'])
            climbing = int(request.POST['climbing'])
            breathing = int(request.POST['breathing'])

            alsfrs = speech+salivation+swallowing+handwriting + \
                cutting+dressing+turning_in_bed+walking+climbing+breathing

            symptom_duration = float(request.POST['symptom_duration'])
            pulse = float(request.POST['pulse'])
            systolic_blood_pressure = float(
                request.POST['systolic_blood_pressure'])

            result = get_prediction(sexe, age, poids, taille, salivation, cutting, turning_in_bed,
                                    alsfrs, symptom_duration, pulse, systolic_blood_pressure)

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

                speech=speech,
                salivation=salivation,
                swallowing=swallowing,
                handwriting=handwriting,
                cutting=cutting,
                dressing=dressing,
                turning_in_bed=turning_in_bed,
                walking=walking,
                climbing=climbing,
                breathing=breathing,

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
