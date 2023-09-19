'''minun_lista = [1, 2, 3, 4, 6, 40, 49]
print(minun_lista)

minun_monikko = [1, 2, 3, 4, 40, 49]
print(minun_monikko)

minun_monikko2 = 1, 2, 3, 4, 5, 6
print(minun_monikko2)

minun_string = "123456"
#muokataan niitö #listan sisältöä voi muokata, mutable
minun_lista[0] = 0
print(minun_lista)
#monikon ja string sisäältä ei voi muoka
minun_monikko[0] = 0
minun_string = "123456"
'''
'''
viikonpäivät = ("maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai")
#päivä= viikonpäivät[3]
#print(päivä)

järjestysnumero = int(input("Anna viikonpäivän järjestysnumero (1-7): "))
#jos käyttäjä syöttää arvon 1
#viikonpäivä = viikonpäivät [0]
viikonpäivä = viikonpäivät[järjestysnumero-1]
print (f"{järjestysnumero}. viikonpäivä on {viikonpäivä}.")
'''
'''
#moniko voidaan purkaa muuttujin
hedelmät = ("Appelsiini", "Banaani", "Omena")
(eka, toka, kolmas) = hedelmät
print (f"Hedelmiä ovat {eka}, {toka} ja {kolmas}.")
'''
#Joukko (set) on järjestämätön tietorakenne, eli sen alkiot voivat olla missä tahansa järjestyksessä.
#Koska joukon alkioille ei ole määritelty järjestystä, ei alkioihin voi myöskään viitata indeksillä.
#Toisin kuin listassa tai monikossa, sama alkio voi esiintyä joukossa vain kertaalleen,
#eli joukossa ei voi olla kahta samansisältöistä alkiota.
"""
minun_monikko = (1, 2, 3, 4, 5, 6)
minun_monikko = (10, 20, 30, 40, 50, 60)
print(minun_monikko)
minun_lista = (1, 2, 3, 4, 5, 6)
minun_lista = (10, 20, 30, 40, 50, 60)
print(minun_lista)

minun_lista2 = (10, 50, 22, 30, 58)
print(minun_lista2)
minun_set2 = {1, 2, 77, 12, 30, 18}
print(minun_set2)

for i in minun_set2:
    print(i)
"""
"""
minun_set = {"Monopoli", "Shakki", "Cluedo"}
print(minun_set)
#minun_set.add('riski')
#print(minun_set)
#minun_set.remove('Shakki')
#print(minun_set)
"""

#sanakirja

oppilat = {'Katri': 28, 'Sara': 25, 'Emma': 22, 'Saed': 18}
#printaan koko sanakirja
#avaimet
for i in oppilat:
    print(i)
#arvot
for i in oppilat:
    print(oppilat[i])
#mitä ovat items #tärkeä (kaikki items)
print(oppilat.items())

#mitkä ovat avainmia saankirja? (nimet .....)
print(oppilat.keys())

#mitkä ovat arvoja sanakirja? (1,2,3,3,..)
print(oppilat.values())

#tarkea
print(oppilat['Emma'])
oppilat['Farhad'] = 55
print(oppilat.items())
#muokata, sillä avain löytyy
oppilat['Emili'] = 12
print(oppilat.items())
#poista items
del oppilat['Farhad']
print(oppilat.items())
#toinen tapa poistaa, tallenna Emma tiedöt muuttujaan
Emma_ikä = oppilat.pop('Emma')
print(f'Emma poistettiin mutta ikä jäi talteen: {Emma_ikä}')
print(oppilat.items())
#luodaan uusi opilas, jolla Emma tiedot
oppilat['Farhad'] = Emma_ikä
print(oppilat.items())
'''
#voit etsiä onko avain sanakirjassa HELPOSTI avainsanan IN kanssa
nimi = input("Anna nimi: ")
if nimi in oppilat:
    print (f"Henkilö {nimi} ikä on {oppilat[nimi]}.")
'''
