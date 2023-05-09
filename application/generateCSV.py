
import csv
from django.http import HttpResponse
from application.models import Patient

# générer un fichier CSV a partir de la base de donnée


def generer_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="patients.csv"'

    writer = csv.writer(response, delimiter=',')
    patients = Patient.objects.all()

    # Écrire les en-têtes de colonnes dans le fichier CSV
    writer.writerow(['Nom', 'Prenom', 'Sexe', 'Age', 'Poids', 'Taille', 'Speech', 'Salivation', 'Swallowing', 'Handwriting', 'Cutting', 'Dressing',
                    'Turning in bed', 'Walking', 'Climbing', 'Breathing', 'ALSFRS', 'Symptom duration', 'Pulse', 'Systolic blood pressure', 'Prediction', 'Vivant', 'Mort'])

    patients = Patient.objects.all().values_list('nom', 'prenom', 'sexe', 'age', 'poids', 'taille', 'speech', 'salivation', 'swallowing', 'handwriting', 'cutting',
                                                 'dressing', 'turning_in_bed', 'walking', 'climbing', 'breathing', 'alsfrs', 'symptom_duration', 'pulse', 'systolic_blood_pressure', 'prediction', 'vivant', 'mort')

    # Écrire les données de chaque patient dans le fichier CSV
    for patient in patients:
        writer.writerow([patient[0], patient[1], patient[2], patient[3], patient[4], patient[5], patient[6], patient[7], patient[8], patient[9], patient[10], patient[11],
                        patient[12], patient[13], patient[14], patient[15], patient[16], patient[17], patient[18], patient[19], patient[20], patient[21], patient[22]])

    return response
