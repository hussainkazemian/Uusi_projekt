import math


def laskee_yksikkon_pizza(halkaisija, hinta): #halkaisija ja hinta as parameters (function body will go here)
    sade = halkaisija / 2 #calculate the sade of the pizza by dividing the diameter by 2:
    pinta_ala = math.pi * halkaisija ** 2 #calculate the area of the pizza using the formula 'area =π * radius^2`:
    yksikkonhinnan = hinta / pinta_ala #calculate unit price per dividing the price by the area
    return yksikkonhinnan
#define a mian program, user to enter the diameter and
#price of two pizza, calls the hinta_neliometer function
#for each pizza and determine the pizza with lower unit price:
def main():
    halkaisija1 = float(input("Anna ensi pizzan halkaisjan neliometrista: "))
    hinta1 = float(input("Anna ensi pizzan hinnan eurosta: "))
    halkaisija2 = float(input("Anna toinen pizzan halkaisjan neliometrista:"))
    hinta2 = float(input("Anna toinen pizzan hinnan eurosta: "))
    yksikkonhinnan1 = laskee_yksikkon_pizza(halkaisija1, hinta1)
    yksikkonhinnan2 = laskee_yksikkon_pizza(halkaisija2, hinta2)
    if yksikkonhinnan1 < yksikkonhinnan2:
        print("se on alhaisempi ysikoinhinnasta.")
    elif yksikkonhinnan2 < yksikkonhinnan1:
        print("Toinen on paremmin hinnosta")
    else:
        print("Ei ole mitään eroa hinnasta.")

    main()
