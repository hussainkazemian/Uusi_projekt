def poistu_parittomat_luvut(numeroita): #function body will go here
    parittomat_luvut = [] # initialize an empty list even numbers to store
    for i in numeroita: #loo to iterate ove each number in the original list
        if i % 2 == 0: # check if the number is even  operator'%':
            parittomat_luvut.append(i) #if the number is even. append it to the even numner list
    return parittomat_luvut #after iterating through all the numbers, returm the even_numbers list:
#define a main program that creates a list of integers
#calls the "poistu_parittomat_luvut" function and prints
#both the original and the cut_down list:
def main():
    luvut = [1, 2, 80, 42, 71, 10, 63] #create a list of numbers
    karsitun_lista = poistu_parittomat_luvut(luvut) #shoftlisted list as an argument
    print(f" luvut : {luvut}")
    print(f"karsitun_lista: {karsitun_lista}")
    return
main()