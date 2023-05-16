import pandas as pd
import io
from django.http import HttpResponse, HttpResponseBadRequest, FileResponse
from application.models import Patient
from application.predict import get_prediction
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
    """
    La fonction read_csv prend en entrée un fichier CSV de patients sans prédictions. 
    Elle extrait les informations des patients puis les injecte dans le modèle pour obtenir les prédictions correspondantes. 
    Elle renvoie ensuite une nouvelle page HTML avec toutes les informations des patients incluant leurs prédictions ainsi qu'un nouveau fichier CSV téléchargeable. 
    Si aucun fichier n'a été joint, la fonction renvoie une réponse d'erreur.

    """

    csv_file = request.FILES.get('csv_file')

    result = []
    if csv_file:

        extension_csv = csv_file.name.split('.')[-1].lower()
        if extension_csv != 'csv':
            return HttpResponseBadRequest("Le fichier doit être au format CSV.")

        df = pd.read_csv(csv_file)
        '''
        table_html = df.to_html()
        response = HttpResponse()
        response.write(table_html)
        '''
        columns = ['Prediction', 'Survie', 'Mortalite']
        # return true or false
        missing_columns = [col for col in columns if col not in df.columns]

        if missing_columns:
            df = df.reindex(columns=[*df.columns, *missing_columns])

        for i in range(0, df.shape[0]):
            first_row = df.iloc[[i]]  # lignes

            sex = df.columns[2]
            first_row_sex = first_row.loc[:, sex].astype(float).to_frame().T

            age = df.columns[3]
            first_row_age = first_row.loc[:, age].astype(float).to_frame().T

            poids = df.columns[4]
            first_row_poids = first_row.loc[:,
                                            poids].astype(float).to_frame().T

            taille = df.columns[5]
            first_row_taille = first_row.loc[:,
                                             taille].astype(float).to_frame().T

            speech = df.columns[6]
            first_row_speech = first_row.loc[:,
                                             speech].astype(float).to_frame().T

            salivation = df.columns[7]
            first_row_salivation = first_row.loc[:, salivation].astype(
                float).to_frame().T

            swallowing = df.columns[8]
            first_row_swallowing = first_row.loc[:, swallowing].astype(
                float).to_frame().T

            handwritting = df.columns[9]
            first_row_handwritting = first_row.loc[:, handwritting].astype(
                float).to_frame().T

            cutting = df.columns[10]
            first_row_cutting = first_row.loc[:,
                                              cutting].astype(float).to_frame().T

            dressing = df.columns[11]
            first_row_dressing = first_row.loc[:,
                                               dressing].astype(float).to_frame().T

            turning_in_bed = df.columns[12]
            first_row_turning = first_row.loc[:, turning_in_bed].astype(
                float).to_frame().T

            walking = df.columns[13]
            first_row_walking = first_row.loc[:,
                                              walking].astype(float).to_frame().T

            climbing = df.columns[14]
            first_row_climbing = first_row.loc[:,
                                               climbing].astype(float).to_frame().T

            breathing = df.columns[15]
            first_row_breathing = first_row.loc[:, breathing].astype(
                float).to_frame().T

            alsfrs = df.columns[16]
            first_row_alsfrs = first_row.loc[:,
                                             alsfrs].astype(float).to_frame().T

            symptom_duration = df.columns[17]
            first_row_duration = first_row.loc[:, symptom_duration].astype(
                float).to_frame().T

            pulse = df.columns[18]
            first_row_pulse = first_row.loc[:,
                                            pulse].astype(float).to_frame().T

            systolic_blood_pressure = df.columns[19]
            first_row_blood = first_row.loc[:, systolic_blood_pressure].astype(
                float).to_frame().T

            result.append(get_prediction(first_row_sex, first_row_age, first_row_poids, first_row_taille, first_row_salivation, first_row_cutting,
                                         first_row_turning, first_row_alsfrs, first_row_duration, first_row_pulse, first_row_blood))

            df.loc[i, 'Prediction'] = result[i][2]
            df.loc[i, 'Survie'] = result[i][1]
            df.loc[i, 'Mortalite'] = result[i][2]

        buffer = io.BytesIO()
        df.to_csv(buffer, index=False)
        buffer.seek(0)
        response = FileResponse(
            buffer, as_attachment=True, filename='predictions.csv')
        """
            df.insert(20, "prédiction", result[i][2])
            df.insert(21, "chance survie", result[i][1])
            df.insert(22, "chance mort", result[i][0])
        """
        # col = df[[sex]]

        # response.write(first_row_salivation.to_html(header=False, index=False))

        # afficher les chances de mort survie de chaque patient

        # response.write(result)
        '''
        response.write(result[0][0])  # mort patient 0
        response.write("<br>")
        response.write(result[0][1])  # survie patient 0
        response.write("<br>")
        response.write(result[0][2])  # prediction
        '''
        return response
    else:
        return HttpResponseBadRequest("Aucun fichier n'a été joint.")
