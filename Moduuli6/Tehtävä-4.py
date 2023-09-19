def laske_numero(numeroita): #function body will go (lukujen_summma)
    summa = 0 #reset the code will go here
    for i in numeroita: #loop and rest of the code will go here
        summa += i #add each number to the summa
    return summa #return the final summa
#define a main program that creates a list of integers
#calls the laske_numero function and print the returned value:

def main():
    numerot = [1, 5, 8, 9, 10] # list of nummers
    lukujen_summa = laske_numero(numerot) #call this function as an argument
    print(f"lukujen summa on: {lukujen_summa}") #the return value is storedd in the variable lukujen_summa
    return
main()