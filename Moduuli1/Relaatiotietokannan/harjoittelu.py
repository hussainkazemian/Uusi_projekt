import mysql.connector
connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password = 'Dars0023',
         autocommit=True
         )
"""
cursor = connection.cursor()
cursor.execute("SELECT iso_country, name FROM country WHERE iso_country = 'FI'")
result = cursor.fetchone() #hake vain ensimäinen tulosrivin
cursor.execute("SELECT iso_country, name FROM country")
#result = cursor.fetchone()
#print(result)

#result = cursor.fetchone()
#print(result)
result = cursor.fetchall()
print(cursor.rowcount) #tulosrivin määrä
print(result) #koko tulosjoukko listana 
for country in result: #country: yksi tulosjoukon rivi monikkona
    print(f"Maa: {country[1]}, koodi: {country[0]}")
"""
def get_country_by_iso_code(iso_code):
    cursor = connection.cursor()
    sql = f"SELECT iso_country, name FROM country WHERE iso_country = '{iso_code}'"
    cursor.execute(sql)
    #cursor.execute(f"SELECT iso_country, name FROM country WHERE iso_country = '{iso_code}'")
    result = cursor.fetchone()  # hake vain ensimäinen tulosrivin
    if result:
        return result[1]
    else:
        return "NO result."
country = get_country_by_iso_code('FI')
print(country)
country = get_country_by_iso_code(input("syödä maakoodi: "))
print(country)

#päivtetaan maiden nimiä kannassa
def update_country_by_iso_code(iso_code, country_name):
    cursor = connection.cursor()
    sql = f"UPDATE country SET name = '{country_name}' country WHERE iso_country = '{iso_code}'"
    cursor.execute(sql)
    #cursor.execute(f"SELECT iso_country, name FROM country WHERE iso_country = '{iso_code}'")
    #result = cursor.fetchone()  # hake vain ensimäinen tulosrivin
    #if result:
     #   return result[1]
    #lse:
    #    return "NO result."
#country = get_country_by_iso_code('FI')
#print(country)
#country = get_country_by_iso_code(input("syödä maakoodi: "))
#print(country)
    return
update_country_by_iso_code("se", "RUOTSI")
