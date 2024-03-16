import pandas as pd
import matplotlib.pyplot as plt



# Cas moyen
tri_insertion = pd.DataFrame({
    "Taille(N)": [0, 1000, 2000, 3000, 4000, 6000, 7000, 8000, 9000, 10000],
    "Temps (s)": [0, 0.002, 0.005, 0.01, 0.02, 0.05, 0.07, 0.1, 0.12, 0.15]
})

tri_par_sélection = pd.DataFrame({
    "Taille(N)": [0, 1000, 2000, 3000, 4000, 6000, 7000, 8000, 9000, 10000],
    "Temps (s)": [0, 0.006, 0.008, 0.012, 0.03, 0.05, 0.08, 0.12, 0.16, 0.2]
})

tri_gnome = pd.DataFrame({
    "Taille(N)": [0, 1000, 2000, 3000, 4000, 6000, 7000, 8000, 9000, 10000],
    "Temps (s)": [0, 0.001, 0.002, 0.003, 0.008, 0.01, 0.015, 0.02, 0.025, 0.03]
})

tri_rapide = pd.DataFrame({
    "Taille(N)": [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],
    "Temps (s)": [0.0,0.001,0.004,0.01,0.017,0.02574,0.035808,0.04844,0.06202,0.0803,0.09427]
})

tri_bulles = pd.DataFrame({
    "Taille(N)": [0, 1000, 2000, 3000, 4000, 5000, 7000, 8000, 9000, 10000],
    "Temps (s)": [0, 0.01300,  0.0170, 0.03009,0.0530,0.05836, 0.06036, 0.06656,0.072370,0.08531]
})

Tri_Cocktail = pd.DataFrame({
    "Taille(N)": [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],
    "Temps (s)": [0.000000, 0.077000 ,0.158000, 0.244000, 0.320000, 0.354000, 0.438000, 0.528000, 0.585000, 0.629000, 0.649000]
})

tri_fusion = pd.DataFrame({
    "Taille(N)":[1000,2000,3000,4000,5000,6000,7000,8000,9000,10000],
    "Temps (s)": [0.000604,0.001530,0.001419,0.002541,0.001456,0.002208,0.004056,0.002490,0.003042,0.004821]
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
plt.title("Temps d'exécution de tout les algorithmes en C (Pire Cas)")
plt.xlabel("Taille de la liste")
plt.ylabel("Temps (s)")

#Légende                                                                                                         
plt.legend()

#Limiter les axes y
axes.set_ylim([0,0.5])
# Afficher le graphique
plt.show() 

