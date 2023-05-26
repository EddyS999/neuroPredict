import np
import pickle
import sklearn
import os


def get_prediction(sexe, age, poids, taille, salivation, cutting, turning, alsfrs, symptom_duration, pulse, systolic_blood_pressure):
    result = []
    if os.path.getsize('application/model/als_model.pkl') > 0:
        with open('application/model/als_model.pkl', 'rb') as file:
            model = pickle.load(file)
        with open('application/model/als_model.pkl', 'wb') as file:
            pickle.dump(model, file)

        patient = np.array([sexe, age, poids, taille, salivation, cutting,
                           turning, alsfrs, symptom_duration, pulse, systolic_blood_pressure])
        prediction = model.predict(patient.reshape(1, -1))[0]
        probabilite = model._predict_proba_lr(patient.reshape(1, -1))[0]
        result = probabilite.tolist()
        result.append(prediction)

    else:
        return 0
    # on retourne une liste contenant : [chance mort, chance survie, prediction]
    return result


def get_prediction_reg(sexe, age, poids, taille, salivation, cutting, turning, alsfrs, symptom_duration, pulse, systolic_blood_pressure):

    if os.path.getsize('application/model/als_model_reg.pkl') > 0:
        with open('application/model/als_model_reg.pkl', 'rb') as file:
            model = pickle.load(file)
        with open('application/model/als_model_reg.pkl', 'wb') as file:
            pickle.dump(model, file)

        patient = np.array([sexe, age, poids, taille, salivation, cutting,
                           turning, alsfrs, symptom_duration, pulse, systolic_blood_pressure])
        prediction = model.predict(patient.reshape(1, -1))[0]
        return prediction.tolist()

    else:
        return []
