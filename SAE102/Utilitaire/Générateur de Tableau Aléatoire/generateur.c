#include <stdlib.h>
#include <stdio.h>


int main() {

    // Initialisation du chemin d'accès (relatif à l'ordinateur)
    const char *path = "C:\\Users\\but-info\\Documents\\BUT-INFO\\S1\\SAE\\SAE1.02\\Table\\" ;

    // Initialisation de la variable n qui va générer un tableau aléatoire de taille N
    int n;

    // Demande à l'utilisateur la taille N du tableau
    printf("Nombres :");
    scanf("%d", &n);

    // Création du nom du fichier avec le chemin d'accès + nom du fichier
    char filename[100];
    sprintf(filename, "%s%d.txt", path, n);


    // Ouverture du fichier
    FILE* fichier = fopen(filename, "w") ;

    int limite = n;
    srand( (unsigned int) time(NULL));
    printf("Tirage de 10 nombres aleatoires entre 0 et %d\n", n);


    if (fichier != NULL){

        // Ecriture ligne par ligne de valeur généré  aléatoirement
        for (int i=0; i<n; i++) {
        // tirage d'un nombre aléatoire dans l'intervalle [0,limite[
            int nb = (int)(((float) rand()/ RAND_MAX) * limite);

            fprintf(fichier,"%d\n", nb);
        }
    }

            fclose(fichier);

    return 0;





}
