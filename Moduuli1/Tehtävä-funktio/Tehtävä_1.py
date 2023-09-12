import random
def pelialka():
    kerrat = random.randint(1, 6)
    while kerrat != 6:
        print(kerrat)
        kerrat = random.randint(1, 6)
    print("saat oikein 6")
    return
pelialka()
"""
#toinentavalla
import random
def dice():
    kerrat = random.randint(1, 6)
    while kerrat != 6:
        print(kerrat)
        kerrat = random.randint (1, 6)
    print("saat oikein")
    return
dice()
"""