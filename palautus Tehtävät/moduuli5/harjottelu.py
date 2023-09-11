name1= "anrea"
name2= "James"
name3= "kate"
age1= 5
age2= 15.5
age3= 66
print(f"{name1}, ikä {age1} vuotta")
print(f"{name2}, ikä {age2} vuotta")
print(f"{name3}, ikä {age3} vuotta")
print("--------------")
names = ["Anrea", "James", "kate", "ahmad", "Jaf", "david", "hashem"]
ages= [5, 15.5, 66, 50, 20, 44, 25]
#alkioon viitataan indeksinumerolla
#print(f"{names[0]}, ikä {ages[0]} vuotta")
#listan läpikäynti while-silmukalla
iterator = 0
while iterator < len(names): #<3
    print(f"{names[iterator]}, ikä {ages[iterator]} vuotta")
    iterator += 1

#eri tapoja viitata alkioihin
print(names[0:5]) #viisi alkoita alkaan indeksillä 2 edelleen lista-muodossa
print(names[-1]) #-1 viittaa aina viimeiseen'
print(names[3:]) #kaikki loput alkiot lakaen indeksillä 3 lista-muodossa
#listan pittus len()
lenght = len(names)
print(lenght)

names.append("uusi nimi") #uusi alkio listan loppuun
names.remove("ahmad") #poistaa ekan "ahmad" -arvon
names.insert(0, "ahmad") #lisää uuden alkion haluttuun kohtaan (tässä alkuun indeksi)
print(names)
names.extend(ages) # ei virhettä muttta yleensä huono käytäntö yhditää erityyppidiä
print(names)
#print(names.index(15.5)) lis ata uudesta

newName= input("Anna uusi name: ") #käyttäjän syötteen lisääminen listaan
#names.append(newName)
#onko joku tietty arvo listalla?
searchterm = input("ketä etsit:?")
if searchterm in names:
    print(f"arvo {searchterm} löytyy listalta")
else:
    print("ei löytyy")
print("for-loop esim.")
print(names)
# lista alkioiden läpikäynttii for_silmukka
for name in names:
    print(f"name: {name}")
#for-silmukka iteraattorilla
for i in range (7):
    print(f"Nimi: {names[i]})
for i in range(len(names)): #0, 1, 2, 3, 4,  ...names-listan pituus-1
    print(f"Nimi: {names[i]}, ikä: {ages[i]}")
#range ()esimerkkejä
for i in range(12, 25, 3):
    print(i)