from django.db import models

# test
# Create your models here.


class Patient(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    sexe = models.IntegerField()
    age = models.IntegerField()
    poids = models.FloatField()
    taille = models.FloatField()
    # ALSFRS
    speech = models.IntegerField(default=0)
    salivation = models.IntegerField(default=0)
    swallowing = models.IntegerField(default=0)
    handwriting = models.IntegerField(default=0)
    cutting = models.IntegerField(default=0)
    dressing = models.IntegerField(default=0)
    turning_in_bed = models.IntegerField(default=0)
    walking = models.IntegerField(default=0)
    climbing = models.IntegerField(default=0)
    breathing = models.IntegerField(default=0)
    alsfrs = models.IntegerField()

    symptom_duration = models.FloatField(max_length=4)
    pulse = models.FloatField(max_length=4)
    systolic_blood_pressure = models.FloatField(max_length=4)
    prediction = models.IntegerField()
    vivant = models.FloatField(max_length=100)
    mort = models.FloatField(max_length=100)

    def __str__(self) -> str:
        return self.nom
