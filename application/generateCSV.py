
import pandas as pd
from django.http import HttpResponse
from application.models import Patient

# générer un fichier CSV a partir de la base de donnée


def generer_csv(request):
    info = Patient.objects.all()
    df = pd.DataFrame(list(info.values()))
    fichier = "donnees.csv"
    response = HttpResponse(content='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{fichier}"'
    df.to_csv(response, index=False)
    return response
