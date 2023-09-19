"""def nestegallon_litrsta (gallonmäärä):
    litra = gallonmäärä * 3.785
    print(litra)
    return litra
def(main)
"""

def gallon_literkis(gallon):
    litra = gallon * 3.785
    return litra
def main():
    while True:
        gallon = float(input("Anna gallon määrä: (jos anna negatiivinen määrä ohjemisto lopettaa): "))
        if gallon < 0:
            break
        litra = gallon_literkis(gallon)
        print("gallon määrä:", litra)
main()