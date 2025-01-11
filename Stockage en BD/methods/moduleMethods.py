import sqlite3


def ajouter_module():
    # Ajouter un nouveau module
    nom_module = input("Entrez le nom du module : ")
    nom_prof = input("Entrez le nom du professeur pour ce module : ")

    connection = sqlite3.connect("scolarite.db")
    cursor = connection.cursor()

    # Trouver l'ID du professeur basé sur le nom fourni
    cursor.execute("SELECT ID FROM Prof WHERE Nom = ?", (nom_prof,))
    result = cursor.fetchone()

    if result:
        prof_id = result[0]
        cursor.execute("INSERT INTO Module (Module_name, prof_id) VALUES (?, ?)",
                       (nom_module, prof_id))
        connection.commit()
        print("Module ajouté avec succès !")
    else:
        print("Professeur non trouvé !")

    connection.close()


def supprimer_module():
    # Supprimer un module
    module_id = input("Entrez l'ID du module à supprimer : ")

    connection = sqlite3.connect("scolarite.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Module WHERE id = ?", (module_id,))
    connection.commit()
    connection.close()
    print("Module supprimé avec succès !")

def afficher_modules():
    # Afficher tous les modules
    connection = sqlite3.connect("scolarite.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Module")
    rows = cursor.fetchall()
    connection.close()

    print("\nListe des modules :")
    for row in rows:
        print(row)

def MettreaJourModule():
    # Mettre à jour les informations d'un module
    nom_module = input("Entrez le nom du module à mettre à jour : ")
    colonne = input("Entrez la colonne à mettre à jour (Module_name, prof_id) : ")
    nouvelle_valeur = input(f"Entrez la nouvelle valeur pour {colonne} : ")

    connection = sqlite3.connect("scolarite.db")
    cursor = connection.cursor()

    # Trouver l'ID du module basé sur le nom fourni
    cursor.execute("SELECT ID FROM Module WHERE Module_name = ?", (nom_module,))
    result = cursor.fetchone()

    if result:
        module_id = result[0]
        cursor.execute(f"UPDATE Module SET {colonne} = ? WHERE ID = ?", (nouvelle_valeur, module_id))
        connection.commit()
        print("Module mis à jour avec succès !")
    else:
        print("Module non trouvé !")

    connection.close()


