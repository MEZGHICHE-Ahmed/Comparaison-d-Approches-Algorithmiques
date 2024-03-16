import pandas as pd
import matplotlib.pyplot as plt



# Cas moyen
tri_insertion = pd.DataFrame({
    "Taille(N)": [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],
    "Temps (s)": [0, 0.025, 0.045, 0.07555, 0.12855, 0.25, 0.4, 0.65, 0.84, 1.2, 1.5]
})

tri_par_sélection = pd.DataFrame({
    "Taille(N)": [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],
    "Temps (s)": [0.0000, 0.0208, 0.0833, 0.1810, 0.3458, 0.4, 0.5669, 0.6484, 1.0068, 1.2550, 1.4064]
})

tri_gnome = pd.DataFrame({
    "Taille(N)": [0, 100, 200, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],
    "Temps (s)": [0, 0.000000, 0.000000, 0.016, 0.035, 0.1, 0.3, 0.6, 1.2, 1.8, 2.5, 3.5, 5.0, 6.0]
})

tri_rapide = pd.DataFrame({
    "Taille(N)": [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],
    "Temps (s)": [0.0,0.0385,0.1528,0.3443,0.6195,0.9863,1.474,1.9335,2.474,4.4523,5.374]
})

tri_bulles = pd.DataFrame({
    "Taille(N)": [0, 1000, 2000, 3000, 4000, 5000, 7000, 8000, 9000, 10000],
    "Temps (s)": [0, 0.043474,  0.180716, 0.42409,0.943082,0.9452, 1.252564, 1.635368, 2.11326,2.58462]
})

Tri_Cocktail = pd.DataFrame({
    "Taille(N)": [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],
    "Temps (s)": [0.000000, 0.046617, 0.205789, 0.425013, 0.512001, 1.235652, 1.851067, 2.451070, 3.284093, 4.094731, 5.247000]
})

tri_fusion = pd.DataFrame({
    "Taille(N)":[1000,2000,3000,4000,5000,6000,7000,8000,9000,10000],
    "Temps (s)": [0.0,0.0,0.014,0.008 ,0.016 ,0.016,0.015,0.029 ,0.022,0.031]
}) 





#affichage
axes = plt.gca()
axes.plot(tri_insertion["Taille(N)"], tri_insertion["Temps (s)"], label="Tri Insertion")
plt.scatter(tri_insertion["Taille(N)"], tri_insertion["Temps (s)"])
axes.plot(tri_par_sélection["Taille(N)"], tri_par_sélection["Temps (s)"], label="Tri Sélection")
plt.scatter(tri_par_sélection["Taille(N)"], tri_par_sélection["Temps (s)"])
axes.plot(tri_gnome["Taille(N)"], tri_gnome["Temps (s)"], label="Tri Gnome")
plt.scatter(tri_gnome["Taille(N)"], tri_gnome["Temps (s)"])
axes.plot(tri_rapide["Taille(N)"], tri_rapide["Temps (s)"], label="Tri Rapide")
plt.scatter(tri_rapide["Taille(N)"], tri_rapide["Temps (s)"])
axes.plot(tri_bulles["Taille(N)"], tri_bulles["Temps (s)"], label="Tri Bulles")
plt.scatter(tri_bulles["Taille(N)"], tri_bulles["Temps (s)"])
axes.plot(Tri_Cocktail["Taille(N)"], Tri_Cocktail["Temps (s)"], label="Tri Cocktail")
plt.scatter(Tri_Cocktail["Taille(N)"], Tri_Cocktail["Temps (s)"])
axes.plot(tri_fusion["Taille(N)"],tri_fusion["Temps (s)"], label="Tri Fusion")
plt.scatter(tri_fusion["Taille(N)"], tri_fusion["Temps (s)"])

 

# Titre et étiquettes
plt.title("Temps d'exécution de tout les algorithmes en Python (Pire Cas)")
plt.xlabel("Taille de la liste")
plt.ylabel("Temps (s)")

#Légende                                                                                                         
plt.legend()

#Limiter les axes y
axes.set_ylim([0,0.5])
# Afficher le graphique
plt.show() 

