import os
from Classes.Departement import Departement

FICHIER_DEPARTEMENTS = "./departments.txt"


def lire_departements():
    """Lit les départements depuis le fichier texte."""
    departements = []
    if not os.path.exists(FICHIER_DEPARTEMENTS):
        return departements

    with open(FICHIER_DEPARTEMENTS, "r") as file:
        for ligne in file:
            parts = ligne.strip().split(",")
            if len(parts) == 2:
                departements.append(Departement(nom_department=parts[1]))
    return departements


def ecrire_departements(departements):
    """Écrit les départements dans le fichier texte."""
    with open(FICHIER_DEPARTEMENTS, "w") as file:
        for index, dep in enumerate(departements, start=1):
            file.write(f"{index},{dep.nom_department}\n")


def ajouter_departement():
    """Ajoute un nouveau département."""
    nom_department = input("Entrez le nom du département : ")
    departements = lire_departements()
    nouveau_departement = Departement(nom_department)
    departements.append(nouveau_departement)
    ecrire_departements(departements)
    print("Département ajouté avec succès !")


def afficher_departements():
    """Affiche tous les départements."""
    departements = lire_departements()
    print("\nListe des départements :")
    for index, dep in enumerate(departements, start=1):
        print(f"ID: {index}, Nom: {dep.nom_department}")


def supprimer_departement():
    """Supprime un département par son nom."""
    nom_department = input("Entrez le nom du département à supprimer : ")
    departements = lire_departements()
    departements = [dep for dep in departements if dep.nom_department != nom_department]

    ecrire_departements(departements)
    print("Département supprimé avec succès !")


def mettre_a_jour_departement():
    """Mettre à jour un département par son nom."""
    ancien_nom = input("Entrez le nom actuel du département à modifier : ")
    departements = lire_departements()

    for dep in departements:
        if dep.nom_department == ancien_nom:
            nouveau_nom = input("Entrez le nouveau nom du département : ")
            dep.nom_department = nouveau_nom
            ecrire_departements(departements)
            print("Département mis à jour avec succès !")
            return

    print("Aucun département trouvé avec ce nom.")
