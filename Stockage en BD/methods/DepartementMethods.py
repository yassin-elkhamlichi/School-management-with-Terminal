import sqlite3

def ajouter_departement():
    # Ajouter un nouveau département
    nom_department = input("Entrez le nom du département : ")

    connection = sqlite3.connect("scolarite.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Department (Department_name) VALUES (?)", (nom_department,))
    connection.commit()
    connection.close()
    print("Département ajouté avec succès !")

def supprimer_departement():
    # Supprimer un département
    department_id = input("Entrez l'ID du département à supprimer : ")

    connection = sqlite3.connect("scolarite.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Department WHERE id = ?", (department_id,))
    connection.commit()
    connection.close()
    print("Département supprimé avec succès !")

def afficher_departements():
    # Afficher tous les départements
    connection = sqlite3.connect("scolarite.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Department")
    rows = cursor.fetchall()
    connection.close()

    print("\nListe des départements :")
    for row in rows:
        print(row)

def MettreaJourDepartement():
    # Mettre à jour les informations d'un département
    nom_department = input("Entrez le nom du département à mettre à jour : ")
    nouvelle_valeur = input("Entrez la nouvelle valeur pour Department_name : ")

    connection = sqlite3.connect("scolarite.db")
    cursor = connection.cursor()

    # Trouver l'ID du département basé sur le nom fourni
    cursor.execute("SELECT Id FROM Department WHERE Department_name = ?", (nom_department,))
    result = cursor.fetchone()

    if result:
        department_id = result[0]
        cursor.execute("UPDATE Department SET Department_name = ? WHERE Id = ?", (nouvelle_valeur, department_id))
        connection.commit()
        print("Département mis à jour avec succès !")
    else:
        print("Département non trouvé !")

    connection.close()

