import pandas as pd
import matplotlib.pyplot as plt

# Meilleur cas
best_case = pd.DataFrame({
    "Taille(N)": [100, 200, 1000, 5000, 7500, 10000],
    "Temps (s)": [0.0000, 0.0000, 0.0344, 0.1763, 0.2503, 0.3390]
})

# Cas moyen
average_case = pd.DataFrame({
    "Taille(N)": [100, 200, 1000, 5000, 7500, 10000],
    "Temps (s)": [0.0000, 0.0056, 0.0355, 0.1776, 0.2933, 0.3390 ]
})

# Pire cas
worst_case = pd.DataFrame({
    "Taille(N)": [100, 200, 1000, 5000, 7500, 10000],
    "Temps (s)": [0.0032, 0.0094, 0.0430, 0.2030, 0.3336, 0.4746]
})

# Afficher les courbes
axes = plt.gca()
axes.plot(best_case["Taille(N)"], best_case["Temps (s)"], label="Meilleur cas")
axes.plot(average_case["Taille(N)"], average_case["Temps (s)"], label="Cas moyen")
axes.plot(worst_case["Taille(N)"], worst_case["Temps (s)"], label="Pire cas")

# Titre et étiquettes
plt.title("Temps d'exécution de l'algorithme de Tri Par Insertion")
plt.xlabel("Taille de la liste")
plt.ylabel("Temps (s)")

#Légende                                                                                                         
plt.legend()

#Limiter les axes y
axes.set_ylim([0,0.5])
# Afficher le graphique
plt.show() 

