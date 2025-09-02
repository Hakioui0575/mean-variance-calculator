import numpy as np   # On importe numpy pour faire les calculs

def calculate(lst):
    # Vérifier que la liste contient exactement 9 nombres
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")

    # Transformer la liste en matrice 3x3
    arr = np.array(lst).reshape(3, 3)

    # Créer le dictionnaire avec toutes les statistiques
    calculations = {
        # Moyenne (par colonnes, par lignes, et sur toute la matrice)
        'mean': [
            arr.mean(axis=0).tolist(),   # colonnes
            arr.mean(axis=1).tolist(),   # lignes
            arr.mean().item()            # total
        ],

        # Variance
        'variance': [
            arr.var(axis=0).tolist(),
            arr.var(axis=1).tolist(),
            arr.var().item()
        ],

        # Écart-type
        'standard deviation': [
            arr.std(axis=0).tolist(),
            arr.std(axis=1).tolist(),
            arr.std().item()
        ],

        # Maximum
        'max': [
            arr.max(axis=0).tolist(),
            arr.max(axis=1).tolist(),
            arr.max().item()
        ],

        # Minimum
        'min': [
            arr.min(axis=0).tolist(),
            arr.min(axis=1).tolist(),
            arr.min().item()
        ],

        # Somme
        'sum': [
            arr.sum(axis=0).tolist(),
            arr.sum(axis=1).tolist(),
            arr.sum().item()
        ]
    }

    # Retourner le dictionnaire
    return calculations
