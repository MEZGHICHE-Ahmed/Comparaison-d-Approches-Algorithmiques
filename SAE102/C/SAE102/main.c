#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include "tri.h"
#include "utile.h"

int main() {
    char t[20];
    char c[20];
    int *tab;
    int n;

    clock_t debut; /* temps initial en ticks d’horloge */
    clock_t fin; /* temps final en ticks d’horloge */
    float temps_cpu; /* temps total en secondes */


    printf("Rentré une valeur de votre choix entre : 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000 : ");
    scanf("%d", &n);

    printf("Quelle tri voulez-vous utiliser ? (entre : Bulle, Insertion, Selection, Gnome, Fusion, Cocktail, Rapide) : ");
    scanf("%s", t);

    printf("Quel est le cas ? (entre Meilleur, Pire et Moyen) : ");
    scanf("%s", c);

    // Va chercher quel cas on a écrit pour modifier le tab
    if (strcmp(c, "Meilleur") == 0) {
        tab = meilleurCas(n);
    } else if (strcmp(c, "Pire") == 0) {
        tab = pireCas(n);
    } else if (strcmp(c, "Moyen") == 0) {
        tab = moyenCas(n);
    } else {
        printf("Cas non existant, veuillez réessayer :\n");
        return 1;
    }

    // Va chercher quel tri on a écrit pour trier le tab
    if (strcmp(t, "Bulle") == 0) {
        debut = clock();

        tri_bulle(tab, n);

        fin = clock();

        temps_cpu = (float) (fin - debut) / CLOCKS_PER_SEC;

        printf("Le temps d'exécution est de %f secondes\n", temps_cpu);
    } else if (strcmp(t, "Insertion") == 0) {
        debut = clock();

        TriInsertion(tab, n);

        fin = clock();

        temps_cpu = (float) (fin - debut) / CLOCKS_PER_SEC;

        printf("Le temps d'exécution est de %f secondes\n", temps_cpu);
    } else if (strcmp(t, "Selection") == 0) {
        debut = clock();

        tri_selection(tab, n);

        fin = clock();

        temps_cpu = (float) (fin - debut) / CLOCKS_PER_SEC;

        printf("Le temps d'exécution est de %f secondes\n", temps_cpu);
    } else if (strcmp(t, "Gnome") == 0) {
        struct timeval debut, fin;
        gettimeofday(&debut, NULL);
        tri_gnome(tab, n);
        gettimeofday(&fin, NULL);
        double temps_cpu = (fin.tv_sec - debut.tv_sec) + (fin.tv_usec - debut.tv_usec) / 1000000.0;
        printf("Le temps d'exécution est de %f secondes\n", temps_cpu);
    } else if (strcmp(t, "Fusion") == 0) {
        debut = clock();

        tri_fusion(tab, 0, n-1);

        fin = clock();

        temps_cpu = (float) (fin - debut) / CLOCKS_PER_SEC;

        printf("Le temps d'exécution est de %f secondes\n", temps_cpu);
    } else if (strcmp(t, "Cocktail") == 0) {
        debut = clock();

        triCocktail(tab, n);

        fin = clock();

        temps_cpu = (float) (fin - debut) / CLOCKS_PER_SEC;

        printf("Le temps d'exécution est de %f secondes\n", temps_cpu);
    } else if (strcmp(t, "Rapide") == 0) {
        debut = clock();

        tri_rapide(tab, 0, n-1);

        fin = clock();

        temps_cpu = (float) (fin - debut) / CLOCKS_PER_SEC;

        printf("Le temps d'exécution est de %f secondes\n", temps_cpu);
    } else {
        printf("Tri non existant, veuillez réessayer :\n");
        return 1;
    }

    return 0;
}
