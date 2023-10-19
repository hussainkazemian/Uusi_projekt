def guess_city():
    menu()
    while True:
        screen_refresh()

        ##################### Start #########################

        current_station, game_id = create_game()
        airplane_location = get_airplane(game_id)

        guessed_letters = []  # List to store the guessed letters

        while True:
            screen_refresh()
            moveto(current_station)
            update_balance(-1, game_id)

            ################### STATION MENU ################

            station_name = get_current_station_name(current_station)
            if airplane_location == station_name[0]:
                print("YOU WON!")
                input("...")
                break  # Exit the loop when the city name is guessed
            balance = get_balance(game_id)
            if balance < 0:
                print_text("gameover")
                break

            neighbors = get_neighbors(current_station)
            print(f"\nYou're arriving at {station_name[0]}.\n")
            print(get_story())
            print(f"\nYour balance is {balance} bottles of vodka.")
            print("Connected stations:\n...")

            for choice in neighbors:
                city, city_id = neighbors[choice]
                print(f"{choice}) {city}")
            print("...")

            current_station = input("Where to: ")

            while (current_station not in neighbors) and current_station != 'x':
                print('\n\nWrong input, please try again.')
                for choice in neighbors:
                    city, city_id = neighbors[choice]
                    print(f"{choice}) {city}")
                current_station = input("Where to: ")

            if current_station == 'x':
                break

            city, current_station = neighbors[current_station]

            # Ask player to guess a letter
            letter = input("Guess a letter: ")

            # Add the guessed letter to the list
            guessed_letters.append(letter)
        menu()