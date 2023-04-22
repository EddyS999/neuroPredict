import np
import pickle
import sklearn
import os

fichier = 'model/als_model.pkl'
# Charger le modèle
if os.path.getsize(fichier) > 0:
    with open(fichier, 'rb') as file:
        model = pickle.load(file)
        
    with open(fichier, 'wb') as file:
        pickle.dump(model, file)
# Les caractéristiques d'un patient (Attention l'ordre des variables est important.)
    patient = np.array([0, 55, 75, 175, 4, 4, 4, 30, 22.53, 77.18, 131.71])
# Le résultat du modèle
    print(model.predict(patient.reshape(1, -1)))
# La probabilité que le patient soit mort ou vivant
    print(model._predict_proba_lr(patient.reshape(1, -1)))
else:
    print("erreur de lecture")