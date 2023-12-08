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


def get_all_workouts():

    db = sqlite3.connect()

    query = """ SELECT NAME,REPS,WEIGHT FROM WORKOUTS """

    cur = db.cursor()
    workouts_io = cur.execute(query)
    workouts_list = [i for i in workouts_io]
    db.close()

    return workouts_list


def update_workout(workout_id, workout_rep, workout_weight):

    db = sqlite3.connect('database.db')

    query = """ UPDATE WORKOUTS SET REP = ?, WEIGHT = ? WHERE ID = ?"""

    cur = db.cursor()
    cur.execute(query,(workout_rep,workout_weight,workout_id))
    db.commit()
    db.close()

def delete_workout(workout_id):

    db = sqlite3.connect('database.db')

    query = """ DELETE FROM WORKOUTS WHERE ID = ?"""

    db.execute(query,workout_id)
    db.commit()
    db.close()
