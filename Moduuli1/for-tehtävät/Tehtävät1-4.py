#Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa
# silmälukujen summan.Käytä for-toistorakennetta
"""
import random
kuutioiden_lkm = int(input('Anna kuutioden määrä:'))
silmäluvut = []

luku =random.randint(1,6)
for i in range(kuutioiden_lkm):
    print(i)
    silmäluvut.append(random.randint(1, 6))
print(f"silmäluvut ovat {silmäluvut} ja summa {sum(silmäluvut)}")
"""
#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta
# suuruusjärjestyksessä suurimmasta alkaen. Vihje: listan alkioiden
# lajittelujärjestyksen voi kääntää antamalla sort-metodille
# argumentiksi reverse=True.
"""
luvut = []
suorita = True
while suorita:
   syöte = input('Anna luku, tyhjö merkkijono lopettaa: ')
   if syöte != '':
       luvut.append(int(syöte))
   else:
       suorita = False

print(luvut)
luvut.sort(reverse=True)
print(luvut[0:5])

#vaihtoehto
for i in range(5):
    print(i)
    print(luvut[i])
"""
kaupungit = []
for i in range(5):
    nimi = input("Anna kaupungit nimi: ")
    kaupungit.append(nimi)
for kaupungit in kaupungit:
    print(kaupungit)
