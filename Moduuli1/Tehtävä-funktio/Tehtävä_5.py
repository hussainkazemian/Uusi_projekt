import math
koko1 = float(input("Anna ensimäinen pizzan halkaisijan: "))
hinta1 = float(input("Anna ensimäinen pizzan hinta: "))
koko2 = float(input("Anna toinen halkaisijan: "))
hinta2 = float(input("Anna toinen pizza hinta: "))
def pizzafunktio ():
    pizza1 = math.pi * koko1 ** 2
    pizza2 = math.pi * koko2 ** 2
    euro_per_neliömeter = koko1, koko2 / pizza1, pizza2
    print(f"pizza1 maksa {pizza1} euroa per neliömeter ")
    print(f"pizza2 maksaa {pizza2} euroa per neliömeter")

    pizzafunktio()