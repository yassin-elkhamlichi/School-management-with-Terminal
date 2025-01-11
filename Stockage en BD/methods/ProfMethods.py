import sqlite3
def ajouter_prof():
    # Ajouter un nouveau professeur
    nom = input("Entrez le nom du professeur : ")
    prenom = input("Entrez le prénom du professeur : ")
    email = input("Entrez l'email du professeur : ")
    datanais = input("Entrez la date de naissance du professeur (YYYY-MM-DD) : ")
    tele = input("Entrez le numéro de téléphone du professeur : ")
    adresse = input("Entrez l'adresse du professeur : ")
    nom_department = input("Entrez le nom du département du professeur : ")

    connection = sqlite3.connect("scolarite.db")
    cursor = connection.cursor()

    # Trouver l'ID du département basé sur le nom fourni
    cursor.execute("SELECT Id FROM Department WHERE Department_name = ?", (nom_department,))
    result = cursor.fetchone()

    if result:
        department_id = result[0]
        cursor.execute('''INSERT INTO Prof (Nom, Prenom, Email, Datenais, Tele, Adresse, Department_id) 
                          VALUES (?, ?, ?, ?, ?, ?, ?)''',
                       (nom, prenom, email, datanais, tele, adresse, department_id))

        connection.commit()
        print("Professeur ajouté avec succès !")
    else:
        print("Département non trouvé !")

    connection.close()

def supprimer_prof():
    # Supprimer un professeur
    prof_id = input("Entrez l'ID du professeur à supprimer : ")

    connection = sqlite3.connect("scolarite.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Prof WHERE id = ?", (prof_id,))
    connection.commit()
    connection.close()
    print("Professeur supprimé avec succès !")

def afficher_profs():
    # Afficher tous les professeurs
    connection = sqlite3.connect("scolarite.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Prof")
    rows = cursor.fetchall()
    connection.close()

    print("\nListe des professeurs :")
    for row in rows:
        print(row)

def MettreaJourProf():
    # Mettre à jour les informations d'un professeur
    nom_prof = input("Entrez le nom du professeur à mettre à jour : ")
    colonne = input("Entrez la colonne à mettre à jour (Nom, Prenom, Email, Datanais, Tele, Adresse, Department_id) : ")
    nouvelle_valeur = input(f"Entrez la nouvelle valeur pour {colonne} : ")

    connection = sqlite3.connect("scolarite.db")
    cursor = connection.cursor()

    # Trouver l'ID du professeur basé sur le nom fourni
    cursor.execute("SELECT ID FROM Prof WHERE Nom = ?", (nom_prof,))
    result = cursor.fetchone()

    if result:
        prof_id = result[0]
        cursor.execute(f"UPDATE Prof SET {colonne} = ? WHERE ID = ?", (nouvelle_valeur, prof_id))
        connection.commit()
        print("Professeur mis à jour avec succès !")
    else:
        print("Professeur non trouvé !")

    connection.close()

