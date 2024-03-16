#include <stdio.h>
#include <stdlib.h>

void tri_bulle(int l[], int size) {
    for (int i = 1; i < size; ++i) {
        int key = l[i];
        int j = i - 1;

        while (j >= 0 && l[j] > key) {
            l[j + 1] = l[j];
            j -= 1;
        }

        l[j + 1] = key;
    }

    printf("Tableau après le tri : ");
    for (int i = 0; i < size; ++i) {
        printf("%d ", l[i]);
    }
    printf("\n");
}


void TriInsertion(int tab[], int size) {
    for (int i = 1; i < size; ++i) {
        int temp = tab[i];
        int m = i - 1;

        while (m >= 0 && temp < tab[m]) {
            tab[m + 1] = tab[m];
            m -= 1;
        }

        tab[m + 1] = temp;
    }

    printf("Tableau après le tri : ");
    for (int i = 0; i < size; ++i) {
        printf("%d ", tab[i]);
    }
    printf("\n");
}


void tri_selection(int tableau[], int taille) {
    for (int i = 0; i < taille - 1; ++i) {
        int min_indice = i;
        for (int j = i + 1; j < taille; ++j) {
            if (tableau[j] < tableau[min_indice]) {
                min_indice = j;
            }
        }

        if (min_indice != i) {
            int temp = tableau[i];
            tableau[i] = tableau[min_indice];
            tableau[min_indice] = temp;
        }
    }

    printf("Tableau après le tri : ");
    for (int i = 0; i < taille; ++i) {
        printf("%d ", tableau[i]);
    }
    printf("\n");
}


void tri_gnome(int tableau[], int taille) {
    int ib = 1, i = 2;
    while (ib < taille) {
        if (tableau[ib - 1] <= tableau[ib]) {
            ib = i;
            ++i;
        } else {
            int temp = tableau[ib - 1];
            tableau[ib - 1] = tableau[ib];
            tableau[ib] = temp;
            --ib;
            if (ib == 0) {
                ib = i;
                ++i;
            }
        }
    }

    printf("Tableau après le tri : ");
    for (int i = 0; i < taille; ++i) {
        printf("%d ", tableau[i]);
    }
    printf("\n");
}


void fusion(int tab1[], int len1, int tab2[], int len2, int tab[]) {
    int i = 0, j = 0, k = 0;

    while (i < len1 && j < len2) {
        if (tab1[i] <= tab2[j]) {
            tab[k] = tab1[i];
            i++;
        } else {
            tab[k] = tab2[j];
            j++;
        }
        k++;
    }

    while (i < len1) {
        tab[k] = tab1[i];
        i++;
        k++;
    }

    while (j < len2) {
        tab[k] = tab2[j];
        j++;
        k++;
    }
}


void tri_fusion(int tab[], int debut, int fin) {
    if (debut < fin) {
        int milieu = (debut + fin) / 2;

        int len1 = milieu - debut + 1;
        int len2 = fin - milieu;

        int tab1[len1];
        int tab2[len2];

        // Copie des éléments dans les sous-tableaux temporaires
        for (int i = 0; i < len1; i++) {
            tab1[i] = tab[debut + i];
        }
        for (int j = 0; j < len2; j++) {
            tab2[j] = tab[milieu + 1 + j];
        }

        // Tri des sous-tableaux
        tri_fusion(tab1, 0, len1 - 1);
        tri_fusion(tab2, 0, len2 - 1);

        // Fusion des sous-tableaux triés
        fusion(tab1, len1, tab2, len2, &tab[debut]);
    }
}


void triCocktail(int tab[], int n) {
    int pointD = 0;
    int diminuerN = 1;
    int modif = 1;

    while (modif == 1) {
        modif = 0;

        for (int i = pointD; i < n - diminuerN; ++i) {
            if (tab[i] > tab[i + 1]) {
                modif = 1;
                int transmission = tab[i];
                tab[i] = tab[i + 1];
                tab[i + 1] = transmission;
            }
        }

        if (modif == 1) {
            for (int i = n - diminuerN; i > pointD; --i) {
                if (tab[i] < tab[i - 1]) {
                    int transmission = tab[i];
                    tab[i] = tab[i - 1];
                    tab[i - 1] = transmission;
                }
            }

            ++pointD;
            ++diminuerN;
        }
    }

    printf("Tableau après le tri : ");
    for (int i = 0; i < n; ++i) {
        printf("%d ", tab[i]);
    }
    printf("\n");
}


void tri_rapide(int tab[], int debut, int fin) {
    if (debut < fin) {
        int pivot = tab[fin];
        int i = debut - 1;

        for (int j = debut; j < fin; ++j) {
            if (tab[j] <= pivot) {
                ++i;
                int temp = tab[i];
                tab[i] = tab[j];
                tab[j] = temp;
            }
        }

        int temp = tab[i + 1];
        tab[i + 1] = tab[fin];
        tab[fin] = temp;

        int pivot_index = i + 1;

        tri_rapide(tab, debut, pivot_index - 1);
        tri_rapide(tab, pivot_index + 1, fin);
    }
}
