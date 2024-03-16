import pandas as pd
import matplotlib.pyplot as plt



# Cas Meilleur
tri_insertion = pd.DataFrame({
    "Taille(N)": [0, 100, 200, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],
    "Temps (s)": [0, 0.0000, 0.0038, 0.0040, 0.012, 0.018, 0.026, 0.032, 0.045, 0.05, 0.065, 0.072, 0.09, 0.105]
})

tri_par_sélection = pd.DataFrame({
    "Taille(N)": [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],
    "Temps (s)": [0.0000, 0.0244, 0.0839, 0.1784, 0.3100, 0.4267, 0.6450, 0.8993, 1.0827, 1.3485, 1.6423]
})

tri_gnome = pd.DataFrame({
    "Taille(N)": [0, 100, 200, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],
    "Temps (s)": [0, 0.000000, 0.000000, 0.000000, 0.00000, 0.00000, 0.00001, 0.00002, 0.00003, 0.00004, 0.00005, 0.00006, 0.00007, 0.00008]
})

tri_rapide = pd.DataFrame({
    "Taille(N)": [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],
    "Temps (s)": [0.0,0.03811,0.1552,0.3468,0.6300,1.02,1.43,1.9825,2.687,3.374,4.023]
})

tri_bulles = pd.DataFrame({
    "Taille(N)": [0, 1000, 2000, 3000, 4000, 5000,6000,7000, 8000, 9000, 10000],
    "Temps (s)": [0, 0.000048,  0.00012, 0.000176,0.000208,0.000372, 0.000352, 0.000444, 0.000452,0.000556,0.0006]
})

Tri_Cocktail = pd.DataFrame({
    "Taille(N)": [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],
    "Temps (s)": [0.000000, 0.001045, 0.002002, 0.009123, 0.012001, 0.011574, 0.014296, 0.011008, 0.015132, 0.010826 , 0.038784]
})

tri_fusion = pd.DataFrame({
    "Taille(N)":[1000,2000,3000,4000,5000,6000,7000,8000,9000,10000],
    "Temps (s)": [0.0,0.0,0.017,0.008 ,0.008 , 0.017,0.02,0.023,0.024,0.022]
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
plt.title("Temps d'exécution de tout les algorithmes en Python (Meilleur Cas)")
plt.xlabel("Taille de la liste")
plt.ylabel("Temps (s)")

#Légende                                                                                                         
plt.legend()

#Limiter les axes y
axes.set_ylim([0,0.5])
# Afficher le graphique
plt.show() 

