import random
def heitä_noppa(kerrat):
    luku = random.randint(1, kerrat)
    return luku
def main ():
    max_luku = int(input("Anna maximiluku: "))
    kerrat = 21
    while True:
        luku = heitä_noppa( kerrat)
        print("nopan luku: ", luku)
main()