"meilleurCas = tableau déjà trié par ordre qu'on voulait (ici croissant)"
def meilleurCas(n):
  
    tab = []

    for i in range(n):

        tab.append(i)
    
    print("Tableau avant le tri :", tab)
    return tab

"pireCas = tableau déjà trié mais dans l'ordre inverse de ce qu'on veut (ici décroissant)"
def pireCas(n):
  
    tab = []

    for i in range(n):

        tab.append(n - i - 1)

    print("Tableau avant le tri :", tab)
    return tab

def moyenCas(n):
    f = open("tableauMoyenCas.txt", "r")

    tab = []

    for i in range(int(n)):
        content = f.readline()
        tab.append(int(content.split("\n")[0]))
    f.close()

    print("Tableau avant le tri :", tab)
    return tab