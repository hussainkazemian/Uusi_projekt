#valintarakenne

user_input = input("a vai b?")

if user_input == "a":
    #kodilohko  merkataan nyt sisentämällä 4 välilyöntiä
    print("tee jotain,")
    print("ja jatka sitä")
elif user_input == "b":
    print("käyttäjä valitsi b: een")
    print("tehdään jotain muutta")
elif user_input == "c":
    print("käyttäjä valitsi c:een")

else:
    print("käyttäjä ei syöttänyt a:ta ei b:ta, ei tehdä mitään")


print("ohjelman suoritus jatkuu tästä")

#loogiset opertatorit
age = 5
name = "Hussain"
print(age < 10)
print(name == "Hussain")
print(age < 10 or not name == "Hussain")
#nehaatio kääntöä seuravaan boolean arvon käänteiseksi

print(not True) # =>false
print(not False) # =>true
# = int(input("Anna ikä: "))
age = int(input("Anna ikä:"))
if 15 <= age < 18:  # sama ehto toisin: 15<= age ) and ( age < 18
    paino = float(input("Anna paino (kg): "))
    if paino >= 55:
        print("lääkeen käyttö on sallittua.")
elif age >= 18:
    print("Lääkkeen käyttö on sallittua.")
