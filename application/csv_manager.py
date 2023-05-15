import pandas as pd
from django.http import HttpResponse
from application.models import Patient

# générer un fichier CSV a partir de la base de donnée


def generer_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="patients.csv"'

    patients = Patient.objects.all().values('nom', 'prenom', 'sexe', 'age', 'poids', 'taille', 'speech', 'salivation', 'swallowing', 'handwriting', 'cutting',
                                            'dressing', 'turning_in_bed', 'walking', 'climbing', 'breathing', 'alsfrs', 'symptom_duration', 'pulse', 'systolic_blood_pressure', 'prediction', 'vivant', 'mort')

    # Créer un DataFrame Pandas à partir des données des patients
    df_patients = pd.DataFrame(list(patients))

    # Renommer les colonnes pour correspondre aux en-têtes de colonnes dans le fichier CSV
    df_patients = df_patients.rename(columns={'nom': 'Nom', 'prenom': 'Prenom', 'sexe': 'Sexe', 'age': 'Age', 'poids': 'Poids', 'taille': 'Taille', 'speech': 'Speech', 'salivation': 'Salivation',
                                              'swallowing': 'Swallowing', 'handwriting': 'Handwriting', 'cutting': 'Cutting', 'dressing': 'Dressing', 'turning_in_bed': 'Turning in bed', 'walking': 'Walking',
                                              'climbing': 'Climbing', 'breathing': 'Breathing', 'alsfrs': 'ALSFRS', 'symptom_duration': 'Symptom duration', 'pulse': 'Pulse', 'systolic_blood_pressure': 'Systolic blood pressure',
                                              'prediction': 'Prediction', 'vivant': 'Vivant', 'mort': 'Mort'})

    # Écrire les données dans un fichier CSV et l'envoyer en réponse
    df_patients.to_csv(path_or_buf=response, sep=',', index=False)
    return response


def read_csv(request):
    csv_file = request.FILES.get('csv_file')
    if csv_file:
        df = pd.read_csv(csv_file)
        table_html = df.to_html()
        response = HttpResponse()
        response.write(table_html)
        return response
    else:
        pass
