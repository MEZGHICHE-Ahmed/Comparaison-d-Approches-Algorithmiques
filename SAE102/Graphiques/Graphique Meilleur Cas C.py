import pandas as pd
import matplotlib.pyplot as plt



# Cas moyen
tri_insertion = pd.DataFrame({
    "Taille(N)": [0, 100, 200, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],
    "Temps (s)": [0, 0.0000, 0.0038, 0.0040, 0.012, 0.018, 0.026, 0.032, 0.045, 0.05, 0.065, 0.072, 0.09, 0.105]
})
tri_par_sélection = pd.DataFrame({
    "Taille(N)": [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],
    "Temps (s)": [0.0000, 0.0370, 0.1040, 0.2320, 0.2950, 0.3860, 0.4270, 0.5370, 0.6880, 0.7450, 0.8200]
})
tri_gnome = pd.DataFrame({
    "Taille(N)": [0, 100, 200, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],
    "Temps (s)": [0, 0.000000, 0.000000, 0.000000, 0.00000, 0.00000, 0.00001, 0.00002, 0.00003, 0.00004, 0.00005, 0.00006, 0.00007, 0.00008]
})
tri_rapide = pd.DataFrame({
    "Taille(N)": [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],
    "Temps (s)": [0.00,0.000,0.002,0.007,0.012,0.017,0.025,0.034,0.044,0.056,0.06542]
})
tri_bulles = pd.DataFrame({
    "Taille(N)": [0, 1000, 2000, 3000, 4000, 5000, 7000, 8000, 9000, 10000],
    "Temps (s)": [0, 0.0000, 0.0010, 0.0150,0.0320,0.05558, 0.04546, 0.06132,0.06367,0.07451]
})
Tri_Cocktail = pd.DataFrame({
    "Taille(N)": [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],
    "Temps (s)": [0.000000, 0.081000, 0.118000, 0.223000, 0.268000, 0.334000, 0.365000, 0.473000, 0.507000, 0.557000, 0.573000]
})
tri_fusion = pd.DataFrame({
    "Taille(N)":[1000,2000,3000,4000,5000,6000,7000,8000,9000,10000],
    "Temps (s)": [0.000738,0.001509,0.001545,0.001243,0.002409,0.001292,0.003417,0.003111,0.002849,0.004002]
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
plt.title("Temps d'exécution de tout les algorithmes en C (Meilleur Cas)")
plt.xlabel("Taille de la liste")
plt.ylabel("Temps (s)")

#Légende                                                                                                         
plt.legend()

#Limiter les axes y
axes.set_ylim([0,0.5])
# Afficher le graphique
plt.show() 

