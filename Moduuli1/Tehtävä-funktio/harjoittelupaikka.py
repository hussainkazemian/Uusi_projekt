def print_city(city3):  #(parametria)
    #lokaali muuttuja, arvo käytössä vain funktion sisällä (local scope)
    city= "Espoo"

    #added
    city2 = "Vatnaa"
    print(city)
    print(city2)
    print(city3) #myös funktion parametria eitelty muttuja on lokaali
def print_city_v2():
        print(city) #tulostaa globaalin muuttuja arvon
# globaali muuttuja, arvo käytössä koko ohjelman laajuisesti (global scope)
city = "Helsinki"
print_city("lähti")
print_city("kirkkonumi")  #tulosta edellen city
print(city)
print_city_v2()
#tässä on kaksi eri asioita,#global scope and local scope