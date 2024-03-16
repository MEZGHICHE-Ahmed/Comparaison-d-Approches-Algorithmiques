// CasUtile.h

#ifndef CAS_UTIL_H
#define CAS_UTIL_H

// Fonction pour le meilleur cas (tableau déjà trié par ordre croissant)
int* meilleurCas(int n);

// Fonction pour le pire cas (tableau déjà trié par ordre décroissant)
int* pireCas(int n);

// Fonction pour le cas moyen (à partir d'un fichier "tableauMoyenCas.txt")
int* moyenCas(int n);

#endif // CAS_UTIL_H

