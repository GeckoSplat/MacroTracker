import sqlite3 as sql


def database():  # only needed to first create DB on computer
    con = sql.connect("macrosdb")
    cur = con.cursor()
    cur.execute(
        """ CREATE TABLE Kcal(                       
    Kcals , Fats , Carbs , Proteins )    
    """
    )
    con.commit()
    con.close()
    print(" DB DONE")


database()
