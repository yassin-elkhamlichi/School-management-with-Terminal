import os
from Classes.Module import Module

FICHIER_MODULES = "modules.txt"


def lire_modules():
    """Lit les modules depuis le fichier texte."""
    modules = []
    if not os.path.exists(FICHIER_MODULES):
        return modules

    with open(FICHIER_MODULES, "r") as file:
        for ligne in file:
            parts = ligne.strip().split(",")
            if len(parts) == 2:  # Vérifie que les deux champs sont présents
                modules.append(Module(
                    nom_module=parts[0],
                    prof_id=parts[1]
                ))
    return modules


def ecrire_modules(modules):
    """Écrit les modules dans le fichier texte."""
    with open(FICHIER_MODULES, "w") as file:
        for module in modules:
            file.write(f"{module.nom_module},{module.prof_id}\n")


def ajouter_module():
    """Ajoute un nouveau module."""
    nom_module = input("Entrez le nom du module : ")
    prof_id = input("Entrez l'ID du professeur responsable du module : ")

    modules = lire_modules()
    nouveau_module = Module(nom_module, prof_id)
    modules.append(nouveau_module)
    ecrire_modules(modules)
    print("Module ajouté avec succès !")


def afficher_modules():
    """Affiche tous les modules."""
    modules = lire_modules()
    print("\nListe des modules :")
    for index, module in enumerate(modules, start=1):
        print(f"ID: {index}, Nom du module: {module.nom_module}, ID du professeur: {module.prof_id}")


def supprimer_module():
    """Supprime un module par son nom."""
    nom_module = input("Entrez le nom du module à supprimer : ")
    modules = lire_modules()
    nouveaux_modules = [module for module in modules if module.nom_module != nom_module]

    if len(nouveaux_modules) < len(modules):
        ecrire_modules(nouveaux_modules)
        print("Module supprimé avec succès !")
    else:
        print("Aucun module trouvé avec ce nom.")


def mettre_a_jour_module():
    """Met à jour les informations d'un module par son nom."""
    nom_module = input("Entrez le nom actuel du module à modifier : ")
    modules = lire_modules()

    for module in modules:
        if module.nom_module == nom_module:
            print("\nChamps disponibles : nom_module, prof_id")
            champ = input("Quel champ souhaitez-vous modifier ? ").strip()
            nouvelle_valeur = input(f"Entrez la nouvelle valeur pour {champ} : ")

            if champ in ["nom_module", "prof_id"]:
                setattr(module, champ, nouvelle_valeur)  # Met à jour l'attribut choisi
                ecrire_modules(modules)
                print("Module mis à jour avec succès !")
                return
            else:
                print("Champ invalide !")
                return

    print("Aucun module trouvé avec ce nom.")
