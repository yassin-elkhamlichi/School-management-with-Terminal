import os
from Classes.Prof import Prof

FICHIER_PROFS = "profs.txt"

def lire_profs():
    """Lit les professeurs depuis le fichier texte."""
    profs = []
    if not os.path.exists(FICHIER_PROFS):
        return profs

    with open(FICHIER_PROFS, "r") as file:
        for ligne in file:
            parts = ligne.strip().split(",")
            if len(parts) == 7:  # Vérifie que tous les champs sont présents
                profs.append(Prof(
                    nom=parts[0],
                    prenom=parts[1],
                    email=parts[2],
                    datanais=parts[3],
                    tele=parts[4],
                    adresse=parts[5],
                    department_id=parts[6]
                ))
    return profs


def ecrire_profs(profs):
    """Écrit les professeurs dans le fichier texte."""
    with open(FICHIER_PROFS, "w") as file:
        for prof in profs:
            file.write(f"{prof.nom},{prof.prenom},{prof.email},{prof.datanais},"
                       f"{prof.tele},{prof.adresse},{prof.department_id}\n")


def ajouter_prof():
    """Ajoute un nouveau professeur."""
    nom = input("Entrez le nom du professeur : ")
    prenom = input("Entrez le prénom du professeur : ")
    email = input("Entrez l'email du professeur : ")
    datanais = input("Entrez la date de naissance du professeur (YYYY-MM-DD) : ")
    tele = input("Entrez le numéro de téléphone du professeur : ")
    adresse = input("Entrez l'adresse du professeur : ")
    department_id = input("Entrez l'ID du département du professeur : ")

    profs = lire_profs()
    nouveau_prof = Prof(nom, prenom, email, datanais, tele, adresse, department_id)
    profs.append(nouveau_prof)
    ecrire_profs(profs)
    print("Professeur ajouté avec succès !")


def afficher_profs():
    """Affiche tous les professeurs."""
    profs = lire_profs()
    print("\nListe des professeurs :")
    for index, prof in enumerate(profs, start=1):
        print(f"ID: {index}, Nom: {prof.nom}, Prénom: {prof.prenom}, Email: {prof.email}, "
              f"Date de naissance: {prof.datanais}, Téléphone: {prof.tele}, "
              f"Adresse: {prof.adresse}, Département ID: {prof.department_id}")


def supprimer_prof():
    """Supprime un professeur par son nom."""
    nom_prof = input("Entrez le nom du professeur à supprimer : ")
    profs = lire_profs()
    nouveaux_profs = [prof for prof in profs if prof.nom != nom_prof]

    if len(nouveaux_profs) < len(profs):
        ecrire_profs(nouveaux_profs)
        print("Professeur supprimé avec succès !")
    else:
        print("Aucun professeur trouvé avec ce nom.")


def mettre_a_jour_prof():
    """Met à jour les informations d'un professeur par son nom."""
    nom_prof = input("Entrez le nom actuel du professeur à modifier : ")
    profs = lire_profs()

    for prof in profs:
        if prof.nom == nom_prof:
            print("\nChamps disponibles : nom, prenom, email, datanais, tele, adresse, department_id")
            champ = input("Quel champ souhaitez-vous modifier ? ").strip()
            nouvelle_valeur = input(f"Entrez la nouvelle valeur pour {champ} : ")

            if champ in ["nom", "prenom", "email", "datanais", "tele", "adresse", "department_id"]:
                setattr(prof, champ, nouvelle_valeur)  # Met à jour l'attribut choisi
                ecrire_profs(profs)
                print("Professeur mis à jour avec succès !")
                return
            else:
                print("Champ invalide !")
                return

    print("Aucun professeur trouvé avec ce nom.")
