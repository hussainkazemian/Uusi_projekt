kaupungit = []
käyttäjä = input("kirjoitta kaupungin nimet: ")
while käyttäjä!="":
    kaupungit.append(käyttäjä)
    käyttäjä = input("kirjoitta kaupungit nimet: ")
for i in [kaupungit]:
    print(f"{kaupungit} ovat kaupungit nimet")