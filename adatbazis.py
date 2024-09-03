import mysql.connector
from mysql.connector import Error

class Fuszer:
    def __init__(self,id,nev,ar,tomeg,szarmazas,ajanlat):
        self.id =id
        self.nev =nev
        self.ar =ar
        self.tomeg =tomeg
        self.szarmazas =szarmazas
        self.ajanlat = ajanlat

    def __str__(self):

        return f"{self.id} {self.nev} {self.ar} {self.tomeg} {self.szarmazas} {self.ajanlat}"

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            database ="fuszerkeverek"
        )
        if connection.is_connected():
            print(" kapcsolat sikeresen letrejott")
    except Error as e:
        print(f"hiba tortent: {e}")

    return connection
lista = []
def adat_lekeres(connection):
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM keverek")
        result = cursor.fetchall()
        for row in result:
            id = row[0]
            nev = row[1]
            ar = row[3]
            lista.append(Fuszer(id,nev,ar,0,0,0))
    except Error as e:
        print(f"hiba tortent: {e}")
    print(type(result))

 
def main():
    conn = create_connection()
    adat_lekeres(conn)
    for item in lista:
        print(item)
    if conn:
        conn.close()
    

main()



        