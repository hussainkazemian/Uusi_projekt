import random

def roll_dice():
    return random.randint(1, 6)
def main():
    while True:
        result = roll_dice()
        print("Roll:", result)
        if result == 6:
            break

if __name__ == "__main__":
    main()

    import random


    def roll_dice(num_sides):
        return random.randint(1, num_sides)
    def main():
        num_sides = int(input("Enter the number of sides on the dice: "))
        max_roll = roll_dice(num_sides)

        while True:
            result = roll_dice(num_sides)
            print("Roll:", result)
            if result == max_roll:
                break


    if __name__ == "__main__":
        main()