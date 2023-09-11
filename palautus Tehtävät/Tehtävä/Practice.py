#lisaa
x = int(input("kirjoitta ensi numero: "))
y = int(input("kirjoitta toinen numero: "))
total = str(x + y)
print("summa: " + total)
print()
#vahennyslasku
x = int(input("kirjoitta ensi numero: "))
y = int(input("kirjoitta toinen numero: "))
total = str(x - y)
print("vahennyslasku: " + total)
print()
#kertolasku
x = int(input("kirjoitta ensi numero: "))
y = int(input("kirjoitta toinen numero: "))
total = str(x * y)
print("kertolasku: " + total)
print()
#jako
x = int(input("kirjoitta ensi numero: "))
y = int(input("kirjoitta toinen numero: "))
total = str(x / y)
print("jako: " + total)
print()

elif (sukupuoli and hl in range (134, 195)):
    print ("kayttäjä on: Mies ja hemogolobiinarvo on normaali")
elif sukupuoli == "M" and hemogolobiinarvo > 195:
    print("käyttäjä on: Mies ja hemogolobiinarvo on korkea")
else sukupuoli and hemogolobiinarvo < 117:
    print("käyttäja on Niaset ja hemogolobiiniarvo on alhainen")
elif sukupuoli == "N" and hemogolobiinarvo in range (117, 175):
    print("käyttäjä on Naiset ja hemogolobiiniarvo on normaali")
elif sukupuoli and hemogolobiinarvo >175:
    print("käyttäjä on naiset ja hemogolobiiniarvo on korkea")
