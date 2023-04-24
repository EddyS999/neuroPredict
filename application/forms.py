from django import forms
from .models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('nom', 'prenom', 'sexe', 'age', 'poids', 'taille', 'salivation', 'cutting',
                  'turning_in_bed', 'alsfrs', 'symptom_duration', 'pulse', 'systolic_blood_pressure')
