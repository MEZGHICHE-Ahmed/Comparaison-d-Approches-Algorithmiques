import pandas as pd
import matplotlib.pyplot as plt



# Cas moyen
tri_insertion = pd.DataFrame({
    "Taille(N)": [0, 100, 200, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],
    "Temps (s)": [0, 0.0000, 0.0000, 0.015, 0.0355, 0.08, 0.151, 0.257, 0.33, 0.35, 0.4, 0.42, 0.5, 0.55]
})

tri_par_sélection = pd.DataFrame({
    "Taille(N)": [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],
    "Temps (s)": [0.0000, 0.0360, 0.0820, 0.2220, 0.3230, 0.3780, 0.4590, 0.6790, 0.6290, 0.6970, 0.8540]
})
tri_gnome = pd.DataFrame({
    "Taille(N)": [0, 100, 200, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],
    "Temps (s)": [0, 0.000000, 0.000000, 0.000000, 0.00000, 0.01, 0.04, 0.05, 0.11, 0.16, 0.22, 0.3, 0.39, 0.46]
})

tri_rapide = pd.DataFrame({
    "Taille(N)": [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],
    "Temps (s)": [0.0,0.0,0.0,0.004,0.00745,0.01025,0.01245,0.01447,0.01756,0.0185,0.0201]
})

tri_bulles = pd.DataFrame({
    "Taille(N)": [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],
    "Temps (s)": [0, 0.0000, 0.0141, 0.0260,0.0480,0.05558, 0.057, 0.060, 0.06406,0.07150,0.0831]
})

Tri_Cocktail= pd.DataFrame({
    "Taille(N)": [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],
    "Temps (s)": [0.000000, 0.153000, 0.219000, 0.307000, 0.375000, 0.401000, 0.497000, 0.569000, 0.675000, 0.699000, 0.73000]
})

tri_fusion = pd.DataFrame({
    "Taille(N)": [0, 100, 200, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],
    "Temps (s)": [0, 0.000021, 0.000041, 0.0001, 0.001499, 0.002, 0.0025, 0.003, 0.0035, 0.004, 0.0045, 0.005, 0.0055]
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
plt.title("Temps d'exécution de tout les algorithmes en C (Moyen Cas)")
plt.xlabel("Taille de la liste")
plt.ylabel("Temps (s)")

#Légende                                                                                                         
plt.legend()

#Limiter les axes y
axes.set_ylim([0,0.5])
# Afficher le graphique
plt.show() 

