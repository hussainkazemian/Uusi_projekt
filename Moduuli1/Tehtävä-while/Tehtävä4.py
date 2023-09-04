import random
numrndm = random.randint (1, 10)
print(numrndm)
guess = 0
while guess != numrndm:
    guess = int(input("arvo numero: "))
    if guess < numrndm:
        print("arvomasi on liian pieni")
    elif guess > numrndm:
        print("arvomasi on liaan suuri")
    else:
        print("arvosi on oikein")
