import pandas as pd
import matplotlib.pyplot as plt



# Cas moyen
tri_insertion = pd.DataFrame({
    "Taille(N)": [0,1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],
    "Temps (s)": [0, 0.015, 0.03, 0.06, 0.1, 0.2, 0.4, 0.6, 0.8, 1.2, 1.5]
})

tri_par_sélection = pd.DataFrame({
    "Taille(N)": [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],
    "Temps (s)": [0.0000, 0.0205, 0.0828, 0.1582, 0.2917,0.3, 0.4572, 0.6318, 0.9100, 1.0358, 1.4139,]
})

tri_gnome = pd.DataFrame({
    "Taille(N)": [0, 100, 200, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],
    "Temps (s)": [0, 0.000000, 0.000000, 0.000000, 0.01, 0.05, 0.2, 0.4, 0.8, 1.2, 1.8, 2.5, 3.5, 4.0]
})

tri_rapide= pd.DataFrame({
    "Taille(N)": [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],
    "Temps (s)": [0.0,0.0,0.0,0.006,0.009,0.013,0.016,0.018,0.022,0.022,0.024]
})

tri_bulles = pd.DataFrame({
    "Taille(N)": [0, 1000, 2000, 3000, 4000, 5000,6000,7000, 8000, 9000, 10000],
    "Temps (s)": [0, 0.011996,  0.05058, 0.1154,0.20784,0.3257760, 0.470172, 0.641172, 0.8339880,1.080852,1.297884]
})

Tri_Cocktail = pd.DataFrame({
    "Taille(N)": [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],
    "Temps (s)": [0, 0.000000, 0.031671, 0.132575, 0.272457, 0.512001, 1.131265, 1.998211, 2.074989, 2.611102, 3.446703]
})

tri_fusion = pd.DataFrame({
    "Taille(N)":[1000,2000,3000,4000,5000,6000,7000,8000,9000,10000],
    "Temps (s)": [0.011,0.013,0.012,0.011,0.016, 0.012,0.015,0.018,0.021,0.028]
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
plt.title("Temps d'exécution de tout les algorithmes en Python (Moyen Cas)")
plt.xlabel("Taille de la liste")
plt.ylabel("Temps (s)")

#Légende                                                                                                         
plt.legend()

#Limiter les axes y
axes.set_ylim([0,0.5])
# Afficher le graphique
plt.show() 

