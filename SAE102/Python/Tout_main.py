import Tout_les_tris
import time
import utile

#tri sert à savoir quel tri on veut tester
#cas sert à savoir quel cas on veut tester
#tab est le tableau avec n valeur qui sera trié à la fin
tri = []
cas = []
tab = []
n= int(input('Rentré une valeur de votre choix entre : 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000 : '))

#t est pour le tri 
t = input('Quelle tri voulez vous utiliser ? (entre : Bulle,Insertion,Selection,Gnome,Fusion,Cocktail,Rapide) : ')
t = str(t)
tri.append(t)

#c est pour le cas
c = input("Quel est le cas ? (entre Meilleur, Pire et Moyen) : ")
c = str(c)
cas.append(c)

#Va chercher quel cas on a écrit pour modifier le tab
while cas:
    if cas[0] == 'Meilleur':
        tab = utile.meilleurCas(n)
        cas.pop()

    elif cas[0] == 'Pire':
        tab = utile.pireCas(n)
        cas.pop()

    elif cas[0] == 'Moyen':
        tab = utile.moyenCas(n)
        cas.pop()
    
    else:
        cas.pop()
        m = input('Cas non existant veuillez reesayer :')
        cas.append(m)


#Va chercher quel tri on a écrit pour trier le tab
#tri.pop sert à sortir de la boucle
while tri:
    if tri[0] == 'Bulle':
        debut = int (time.time() * 1000)
        Tout_les_tris.tri_bulle(tab)

        #fin programe
        fin = int (time.time() * 1000)
        temps_cpu = (fin - debut) / 1000
        print(f'le temp d execution est de {temps_cpu}')
        tri.pop()
    elif tri[0] == 'Insertion':
        debut = int (time.time() * 1000)
        Tout_les_tris.TriInsertion(tab)

        #fin programe
        fin = int (time.time() * 1000)
        temps_cpu = (fin - debut) / 1000
        print(f'le temp d execution est de {temps_cpu}')
        tri.pop()
    elif tri[0] == 'Selection':
        debut = int (time.time() * 1000)
        Tout_les_tris.tri_selection(tab)

        #fin programe
        fin = int (time.time() * 1000)
        temps_cpu = (fin - debut) / 1000
        print(f'le temp d execution est de {temps_cpu}')
        tri.pop()
    elif tri[0] == 'Gnome':
        debut = int (time.time() * 1000)
        Tout_les_tris.tri_gnome(tab)

        #fin programe
        fin = int (time.time() * 1000)
        temps_cpu = (fin - debut) / 1000
        print(f'le temp d execution est de {temps_cpu}')
        tri.pop()
    elif tri[0] == 'Fusion':
        debut = int (time.time() * 1000)
        Tout_les_tris.tri_fusion(tab)

        #fin programe
        fin = int (time.time() * 1000)
        temps_cpu = (fin - debut) / 1000
        print(f'le temp d execution est de {temps_cpu}')
        tri.pop()
    elif tri[0] == 'Cocktail':
        debut = int (time.time() * 1000)
        Tout_les_tris.triCocktail(tab)

        #fin programe
        fin = int (time.time() * 1000)
        temps_cpu = (fin - debut) / 1000
        print(f'le temp d execution est de {temps_cpu}')
        tri.pop()
    elif tri[0] == 'Rapide':
        debut = int (time.time() * 1000)
        Tout_les_tris.tri_rapide(tab)

        #fin programe
        fin = int (time.time() * 1000)
        temps_cpu = (fin - debut) / 1000
        print(f'le temp d execution est de {temps_cpu}')
        tri.pop()
    else:
        tri.pop()
        m = input('Tri non existant veuillez reesayer :')
        tri.append(m)