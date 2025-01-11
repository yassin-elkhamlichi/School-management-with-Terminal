from Stockage_en_fichier.Methods.DepartementMethods import *
from Stockage_en_fichier.Methods.ProfMethods import *
from Stockage_en_fichier.Methods.ModuleMethods import *

def menu_principal():
    """Affiche le menu principal."""
    print("\n===== Gestion des Données =====")
    print("1. Gérer les Départements")
    print("2. Gérer les Professeurs")
    print("3. Gérer les Modules")
    print("0. Quitter")

def menu_departements():
    """Menu pour la gestion des départements."""
    print("\n--- Gestion des Départements ---")
    print("1. Ajouter un département")
    print("2. Afficher tous les départements")
    print("3. Supprimer un département")
    print("4. Mettre à jour un département")
    print("0. Retour au menu principal")

def menu_profs():
    """Menu pour la gestion des professeurs."""
    print("\n--- Gestion des Professeurs ---")
    print("1. Ajouter un professeur")
    print("2. Afficher tous les professeurs")
    print("3. Supprimer un professeur")
    print("4. Mettre à jour un professeur")
    print("0. Retour au menu principal")

def menu_modules():
    """Menu pour la gestion des modules."""
    print("\n--- Gestion des Modules ---")
    print("1. Ajouter un module")
    print("2. Afficher tous les modules")
    print("3. Supprimer un module")
    print("4. Mettre à jour un module")
    print("0. Retour au menu principal")

def main():
    """Fonction principale pour exécuter l'application."""
    while True:
        menu_principal()
        choix = input("Entrez votre choix : ")

        if choix == "1":  # Gestion des départements
            while True:
                menu_departements()
                choix_dep = input("Entrez votre choix : ")

                if choix_dep == "1":
                    ajouter_departement()
                elif choix_dep == "2":
                    afficher_departements()
                elif choix_dep == "3":
                    supprimer_departement()
                elif choix_dep == "4":
                    mettre_a_jour_departement()
                elif choix_dep == "0":
                    break
                else:
                    print("Choix invalide. Veuillez réessayer.")

        elif choix == "2":  # Gestion des professeurs
            while True:
                menu_profs()
                choix_prof = input("Entrez votre choix : ")

                if choix_prof == "1":
                    ajouter_prof()
                elif choix_prof == "2":
                    afficher_profs()
                elif choix_prof == "3":
                    supprimer_prof()
                elif choix_prof == "4":
                    mettre_a_jour_prof()
                elif choix_prof == "0":
                    break
                else:
                    print("Choix invalide. Veuillez réessayer.")

        elif choix == "3":  # Gestion des modules
            while True:
                menu_modules()
                choix_module = input("Entrez votre choix : ")

                if choix_module == "1":
                    ajouter_module()
                elif choix_module == "2":
                    afficher_modules()
                elif choix_module == "3":
                    supprimer_module()
                elif choix_module == "4":
                    mettre_a_jour_module()
                elif choix_module == "0":
                    break
                else:
                    print("Choix invalide. Veuillez réessayer.")

        elif choix == "0":  # Quitter
            print("Merci d'avoir utilisé l'application ! À bientôt.")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
