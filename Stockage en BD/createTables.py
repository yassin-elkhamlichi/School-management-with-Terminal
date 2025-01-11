import sqlite3

def create_connection():
    conn = sqlite3.connect('scolarite.db')
    return conn

def create_tables(conn):
    with conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS Prof (
                            ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            Nom TEXT NOT NULL,
                            Prenom TEXT NOT NULL,
                            Email TEXT NOT NULL,
                            DateNais TEXT,
                            Tele TEXT,
                            Adresse TEXT,
                            Department_id INTEGER
                        );''')
        conn.execute(
            ''' CREATE TABLE IF NOT EXISTS Module ( 
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Module_name TEXT NOT NULL,
                Prof_id INTEGER,
                FOREIGN KEY (Prof_id) REFERENCES Prof (ID)
                 );''')
        conn.execute(
            '''CREATE TABLE IF NOT EXISTS Department ( 
                Id INTEGER PRIMARY KEY AUTOINCREMENT, 
                Department_name TEXT NOT NULL 
                );''')

conn = create_connection()
create_tables(conn)
