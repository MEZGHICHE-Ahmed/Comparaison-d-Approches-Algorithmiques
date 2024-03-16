#include <stdio.h>
#include <stdlib.h>

int* meilleurCas(int n) {
    int* tab = (int*)malloc(n * sizeof(int));

    for (int i = 0; i < n; ++i) {
        tab[i] = i;
    }

    printf("Tableau avant le tri : ");
    for (int i = 0; i < n; ++i) {
        printf("%d ", tab[i]);
    }
    printf("\n");

    return tab;
}

int* pireCas(int n) {
    int* tab = (int*)malloc(n * sizeof(int));

    for (int i = 0; i < n; ++i) {
        tab[i] = n - i - 1;
    }

    printf("Tableau avant le tri : ");
    for (int i = 0; i < n; ++i) {
        printf("%d ", tab[i]);
    }
    printf("\n");

    return tab;
}

int* moyenCas(int n) {
    FILE* f = fopen("tableauMoyenCas.txt", "r");
    if (f == NULL) {
        perror("Erreur lors de l'ouverture du fichier");
        exit(EXIT_FAILURE);
    }

    int* tab = (int*)malloc(n * sizeof(int));

    for (int i = 0; i < n; ++i) {
        int content;
        fscanf(f, "%d", &content);
        tab[i] = content;
    }

    fclose(f);

    printf("Tableau avant le tri : ");
    for (int i = 0; i < n; ++i) {
        printf("%d ", tab[i]);
    }
    printf("\n");

    return tab;
}
