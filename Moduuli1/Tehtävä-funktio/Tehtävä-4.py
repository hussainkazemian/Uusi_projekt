def lukujen_summa(numeroita):
    summa = sum(numeroita)
    return summa
def main():
    numeroita = ["1, 5, 6, 8, 7"]
    tulos = lukujen_summa(numeroita)
    print("lukujen summa on: ", tulos)

    main()