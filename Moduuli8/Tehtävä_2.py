import mysql.connector
connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password = 'Dars0023',
         autocommit=True
         )
cursor = connection.cursor()
cursor.execute("SELECT iso_country, ident FROM airport WHERE ident = 'FI'")
result = cursor.fetchone() # hakee vain ensimmäisen tulosrivin
cursor.execute("SELECT airport, ident FROM airport")
result = cursor.fetchall()
print(cursor.rowcount)  # tulosrivien määrä
print(result)  # koko tulosjoukko listana
for country in result:  # country: yksi tulosjoukon rivi monikkona
    print(f"Maa: {country[1]}, koodi: {country[0]}")


"""
def get_country_by_iso_code(iso_code):
    cursor = connection.cursor()
    sql = f"SELECT iso_country, name FROM country WHERE iso_country = '{iso_code}'"
    cursor.execute(sql)
    result = cursor.fetchone()  # hakee vain ensimmäisen tulosrivin
    if result:
        return result[1]
    else:
        return "No results."

country = get_country_by_iso_code('FI')
print(country)
country = get_country_by_iso_code(input("Hae maakoodilla: "))
print(country)

# Päivitetään maiden nimiä kannassa
def update_country_by_iso_code(iso_code, country_name):
    cursor = connection.cursor()
    sql = f"UPDATE country SET name='{country_name}' WHERE iso_country = '{iso_code}'"
    cursor.execute(sql)
    if cursor.rowcount > 0:
        return f"koodi {iso_code} päivitetty, uusi maan nimi: {country_name}"
    else:
        return f"Koodia {iso_code} ei löytynyt. Muutoksia ei tehty."

country_code = input("Anna muokattava koodi: ")
new_name = input("Anna maalle uusi nimi: ")
update_result = update_country_by_iso_code(country_code, new_name)
print(update_result)
"""