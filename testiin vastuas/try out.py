import random
import sys
import time

# ... existing code ...

def reveal_letter(station_name, balance):
    if balance >= 1:
        # Check if the player has enough balance to pay
        balance -= 1
        # Deduct the payment from the balance
        letter_index = int(input("Enter the letter index to reveal: "))
        if letter_index < len(station_name):
            revealed_city = list(station_name)
            revealed_city[letter_index] = station_name[letter_index]
            station_name = "".join(revealed_city)
            print("Letter revealed! The city now looks like:", station_name)
        else:
            print("Invalid letter index!")
    else:
        print("Not enough balance to reveal a letter!")

    return station_name, balance


def main():
    menu()
    while True:
        screen_refresh()

        # ... existing code ...

        guessed_letters = []  # list to store the guessed letters

        while True:
            screen_refresh()

            # ... existing code ...

            reveal_prime = input("Do you want to reveal a letter by spending one prime? (Y/N): ")
            if reveal_prime.lower() == "y":
                station_name, balance = reveal_letter(station_name, balance)

            # ... existing code ...


main()