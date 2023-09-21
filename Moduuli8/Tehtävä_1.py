import mysql.connector
connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password = 'Dars0023',
         autocommit=True
         )
def fetch_airport_details(icoa_code):
    #connect to the airport database.
    cursor = connection.cursor()
    query = "SELECT name, municipality FROM airport WHERE ident = ?"


