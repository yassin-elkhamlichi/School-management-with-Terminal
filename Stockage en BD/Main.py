from methods.DepartementMethods import *
from methods.ProfMethods import *
from methods.moduleMethods import *

def menu_principal():
    while True:
        print("\nMenu Principal :")
        print("1. Gérer les professeurs")
        print("2. Gérer les modules")
        print("3. Gérer les départements")
        print("4. Quitter")

        choix = input("Entrez votre choix : ")

        if choix == "1":
            gerer_professeurs()
        elif choix == "2":
            gerer_modules()
        elif choix == "3":
            gerer_departements()
        elif choix == "4":
            print("Fermeture du programme.")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

def gerer_professeurs():
    while True:
        print("\nGérer les Professeurs :")
        print("1. Ajouter un professeur")
        print("2. Supprimer un professeur")
        print("3. Afficher les professeurs")
        print("4. Mettre à jour un professeur")
        print("5. Retour au menu principal")

        choix = input("Entrez votre choix : ")

        if choix == "1":
            ajouter_prof()
        elif choix == "2":
            supprimer_prof()
        elif choix == "3":
            afficher_profs()
        elif choix == "4":
            MettreaJourProf()
        elif choix == "5":
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

def gerer_modules():
    while True:
        print("\nGérer les Modules :")
        print("1. Ajouter un module")
        print("2. Supprimer un module")
        print("3. Afficher les modules")
        print("4. Mettre à jour un module")
        print("5. Retour au menu principal")

        choix = input("Entrez votre choix : ")

        if choix == "1":
            ajouter_module()
        elif choix == "2":
            supprimer_module()
        elif choix == "3":
            afficher_modules()
        elif choix == "4":
            MettreaJourModule()
        elif choix == "5":
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

def gerer_departements():
    while True:
        print("\nGérer les Départements :")
        print("1. Ajouter un département")
        print("2. Supprimer un département")
        print("3. Afficher les départements")
        print("4. Mettre à jour un département")
        print("5. Retour au menu principal")

        choix = input("Entrez votre choix : ")

        if choix == "1":
            ajouter_departement()
        elif choix == "2":
            supprimer_departement()
        elif choix == "3":
            afficher_departements()
        elif choix == "4":
            MettreaJourDepartement()
        elif choix == "5":
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    menu_principal()
