import random
def heitä_noppa():
    kerrat = random.randint(1, 6)
    while kerrat != 6:
        print(kerrat)
        kerrat = random.randint(1, 6)
    print("sait 6")
    return
heitä_noppa()
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