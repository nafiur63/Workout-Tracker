import sqlite3

def create_table():

    db = sqlite3.connect('database.db')

    query = """  CREATE TABLE IF NOT EXISTS WORKOUTS
       (
       ID INTEGER PRIMARY KEY AUTOINCREMENT,
       NAME TEXT NOT NULL,
       REPS INTEGER NOT NULL,
       WEIGHT INTEGER DEFAULT 0 NOT NULL,
       COMPLETED_AT DATETIME DEFAULT CURRENT_TIMESTAMP
       )   """
    
    cur = db.cursor()
    cur.execute(query)
    db.close()


def insert_workout(name,reps,weight):

    db = sqlite3.connect('database.db')

    query = """ INSERT INTO WORKOUTS(NAME, REPS, WEIGHT)
    VALUES (?,?,?)
    """

    cur = db.cursor()
    cur.execute(query, (name,reps,weight))
    db.commit()
    db.close()