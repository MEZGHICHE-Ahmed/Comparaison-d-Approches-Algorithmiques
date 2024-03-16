def tri_bulle(l: list[int]) -> None:
    """Trie la liste fournie à l'aide d'un algorithme de tri à bulles itérative."""
    # Parcours la liste à partir de l'élément 1
    for i in range(1, len(l)):
        # Contrôle l'élément à comparer (key) et son index (j)
        key = l[i]
        j = i - 1

        # Échange les éléments jusqu'à ce que key soit à l'emplacement correct
        while j >= 0 and l[j] > key:
            # Déplace l'élément à sa place
            l[j + 1] = l[j]

            # Actualise l'index
            j -= 1

        # Insère key à la position appropriée
        l[j + 1] = key
    
    print( "Tableau après le tri :",l)


def TriInsertion(tab: list[int]) -> None :
    # Nous commençons par utiliser la boucle itérative for (de 2 jusqu'à la longueur du tableau) afin de réaliser les prochaines instructions nécessaire n fois 
    
    for i in range(1,len(tab)):
        
        # Initialisation de la variable annexe cle qui va être utilisé lors du changement
        
        temp = tab[i]
        m = i - 1

        # Nous utilisons la boucle itérative while afin d'instruire à l'algorithme que tant la valeur de la I ième place du tableau est supérieur à la suivante "(temp<tab[m])"
        # Et que m est inclus dans [1;N] "(m >= 0)", alors nous les échangeons de place afin que la valeur de la M ième place soit inférieur à la suivante,
        # Puis nous reculons d'un cran afin de répéter les mêmes instructions de sorte à ce que le tableau soit trié de tab[1] à tab[m]

        while m >= 0 and temp < tab[m]:

            # Procédure du changement de place avec l'utilisation d'une variable annexe nommé "temp"

            tab[m + 1] = tab[m]
            m -= 1
            tab[m + 1] = temp
    
#Affiche le tableau après Tri

    print("Tableau après le tri :", tab)
   

def tri_selection(tableau):
    taille = len(tableau)
    for i in range(taille - 1):
        min_indice = i
        for j in range(i + 1, taille):
            if tableau[j] < tableau[min_indice]:
                min_indice = j

        if min_indice != i:
            tableau[i], tableau[min_indice] = tableau[min_indice], tableau[i]
    print(tableau)


def tri_gnome(tableau):
    
    ib,i,taille = 1,2,len(tableau)
    while ib < taille:
        if tableau[ib-1] <= tableau[ib]:
            ib,i = i, i+1
        else:
            tableau[ib-1],tableau[ib] = tableau[ib],tableau[ib-1]
            ib -= 1
            if ib == 0:
                ib,i = i, i+1
    print("Tableau après le tri :",tableau)


def tri_fusion(tab: list[int]) -> None:
  """Trie une liste en utilisant le tri fusion.
  Args:
    tab: La liste à trier.
  """
  if len(tab) <= 1:
    return
  milieu = len(tab) // 2
  tab1 = tab[:milieu]
  tab2 = tab[milieu:]
  # Tri des sous-listes
  tri_fusion(tab1)
  tri_fusion(tab2)
  # Fusion des sous-listes triées
  fusion(tab1, tab2, tab)


def fusion(tab1: list[int], tab2: list[int], tab: list[int]) -> None:
  i = 0
  j = 0
  k = 0
  while i < len(tab1) and j < len(tab2):
    if tab1[i] <= tab2[j]:
      tab[k] = tab1[i]
      i += 1
    else:
      tab[k] = tab2[j]
      j += 1
    k += 1
  # Copie les éléments restants de la première liste
  while i < len(tab1):
    tab[k] = tab1[i]
    i += 1
    k += 1
  # Copie les éléments restants de la deuxième liste
  while j < len(tab2):
    tab[k] = tab2[j]
    j += 1
    k += 1


def triCocktail(tab: list[int]) -> None:
  
  n = len(tab)
  pointD = 0
  diminuerN = 1

  # modif est un INT qui sert comme BOOL pour le while (1 pour vrai et 0 pour faux)
  modif = 1

  while modif == 1:

    # On suppose que le tableau est bien dans l'ordre croissant (pour faire sortir de la boucle)
    modif = 0
    # On commence par analyser et comparer les premières valeurs du tableau jusqu'au bout du tableau
    # (moins le nombre de fois qu'on fait le programme afin de ne pas comparer des éléments qu'on sait qui sont forcement les plus grands).
    for i in range(pointD, len(tab) - diminuerN):
      # Si en cas la valeur est supérieure à la valeur à l'indice supérieur alors
      if tab[i] > tab[i + 1]:
        # Finalement l'hypothèse que le tableau est croissant est faux, donc on n'arrete pas le programme car on est pas sur de l'état du tableau
        modif = 1

        # On interchange les valeurs et ainsi leurs indices
        transmission = tab[i]
        tab[i] = tab[i + 1]
        tab[i + 1] = transmission


    # Sert à voir si en cas le tableau n'était pas croissant au début de la boucle (si en cas il était bien croissant alors pas besoin de verifier ^dans l'autre sens)
    if(modif == 1):
      
      for i in range(len(tab) - diminuerN, pointD, -1):
      
        if tab[i] < tab[i - 1]:
          transmission = tab[i]
          tab[i] = tab[i - 1]
          tab[i - 1] = transmission

      pointD += 1

      diminuerN += 1

  print("Tableau après le tri :",tab)

def tri_rapide(tab: list[int]) -> None:
    #Si la taille du tableau est egale ou inferieur à 1, alors pas besoin de le trier
    if len(tab) <= 1:
        return tab

    #debut_fin est un tableau qui va contenir un tuple de deux valeur, un debut et une fin
    debut_fin = []
    #Pour commencer, on utilise 0 comme indice pour le premier élément de la liste et 'len(tab) - 1' pour avoir l'indice du dernier élément dans la liste.
    debut_fin.append((0, len(tab) - 1))

    while debut_fin:
        #Tant qu'il y a des éléments dans 'debut_fin', 'debut' prend la valeur du premier élément du tuple, 'fin' prend le deuxième élément et 'i' prend la valeur de 'debut - 1'.
        debut, fin = debut_fin.pop()
        pivot = tab[fin]
        i = debut - 1 
        #j va de debut à fin, si tab[j] est plus petit que le pivot, alors i prend plus 1, et il est mit au rang de tab[i] qui se trouve au debut du tableau
        for j in range(debut, fin):
            if tab[j] <= pivot:
                i += 1
                tab[i], tab[j] = tab[j], tab[i]
        #À la fin, on prend le pivot et on le place juste après tous les éléments plus petits accumulés grâce à l'indice 'i'. Les éléments restants au-dessus du pivot sont plus grands
        tab[i + 1], tab[fin] = tab[fin], tab[i + 1]
        pivot_index = i + 1
        #Si 'pivot_index - 1' est inférieur à 'debut', cela signifie qu'il n'y a pas d'élément plus petit que le pivot actuel, donc aucun besoin de traitement. Sinon, on traite en ajoutant de 'debut' jusqu'à 'pivot - 1' ('pivot - 1' car on s'occupe des éléments plus petits que le pivot et on exclut le pivot lui-même).
        if pivot_index - 1 > debut:    
            debut_fin.append((debut, pivot_index - 1))
        #Si 'pivot_index + 1' est superieur à 'fin', cela signifie qu'il n'y a pas d'élément plus grand que le pivot actuel, donc aucun besoin de traitement. Sinon, on traite en ajoutant de 'pivot + 1' jusqu'à 'fin' ('pivot + 1' car on s'occupe des éléments plus grand que le pivot et on exclut le pivot lui-même).
        if pivot_index + 1 < fin:
            debut_fin.append((pivot_index + 1, fin))
    #on print le tableau lorsque le traitement est fini
    print("Tableau après le tri :",tab)