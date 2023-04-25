from django import forms
from .models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('nom', 'prenom', 'sexe', 'age', 'poids', 'taille', 'salivation', 'cutting',
                  'turning_in_bed', 'alsfrs', 'symptom_duration', 'pulse', 'systolic_blood_pressure')

        labels = {
            'nom': 'Nom',
            'prenom': 'Prénom',
            'sexe': 'Sexe',
            'age': 'Âge',
            'poids': 'Poids (en kg)',
            'taille': 'Taille',
            'salivation': 'Salivation',
            'cutting': 'Cutting',
            'turning_in_bed': 'Turning in bed',
            'alsfrs': 'ALSFRS',
            'symptom_duration': 'Durée des symptômes (en mois)',
            'pulse': 'Pouls',
            'systolic_blood_pressure': 'Pression artérielle systolique',
        }

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 0:
            raise forms.ValidationError("L'âge ne peut pas être négatif.")
        return age

    def clean_poids(self):
        poids = self.cleaned_data.get('poids')
        if poids < 0:
            raise forms.ValidationError("Le poids ne peut pas être négatif.")
        return poids

    def clean_taille(self):
        taille = self.cleaned_data.get('taille')
        if taille < 0:
            raise forms.ValidationError(
                "La taille ne peut pas être négative.")
        return taille

    def clean_salvation(self):
        salvation = self.cleaned_data.get('salvation')
        if salvation < 0 or salvation > 4:
            raise forms.ValidationError(
                "Donnée mal saisie.")
        return salvation

    def clean_cutting(self):
        cutting = self.cleaned_data.get('cutting')
        if cutting < 0 or cutting > 4:
            raise forms.ValidationError(
                "Donnée mal saisie.")
        return cutting

    def clean_tib(self):
        tib = self.cleaned_data.get('turning_in_bed')
        if tib < 0 or tib > 4:
            raise forms.ValidationError(
                "Donnée mal saisie.")
        return tib

    def clean_alsfrs(self):
        alsfrs = self.cleaned_data.get('alsfrs')
        if alsfrs < 0 or alsfrs > 40:
            raise forms.ValidationError(
                "L'alsfrs doit se situer entre 0 et 40.")
        return alsfrs

    def clean_duration(self):
        duration = self.cleaned_data.get('symptom_duration')
        if duration < 0:
            raise forms.ValidationError(
                "La durée ne peut pas être négative.")
        return duration

    def clean_pulse(self):
        pulse = self.cleaned_data.get('pulse')
        if pulse < 0:
            raise forms.ValidationError("Le poul ne peut pas être négatif.")
        return pulse

    def clean_blood_pressure(self):
        pressure = self.cleaned_data.get('systolic_blood_pressure')
        if pressure < 0:
            raise forms.ValidationError("Le poids ne peut pas être négatif.")
        return pressure
