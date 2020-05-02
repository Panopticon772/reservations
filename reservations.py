# reservations app

# add wait list functionality/queue

# import random module
import random

# import system module
import sys


def main():

    main_menu_options = [
        'Hello, welcome to MyTable! Please choose from the following options: ',
        'Make a reservation',
        'Exit'
    ]

    def display_main_menu_options():
        print(main_menu_options[0])
        print(main_menu_options[1])
        print(main_menu_options[2])

    def total_seats():
        # randomize the total amount of seats in the restaurant
        total = random.randint(10, 25)
        print(f'number of seats in restuarant: {total}')
        return total

    def occupied_seats(total):
        # total occupied seats
        occupied = random.randint(0, total)
        print(f'occupied seats: {occupied}')
        return occupied

    def available_seats(total, occupied):
        # available seats
        available = total - occupied
        print(f'available seats: {available}')
        return available

    def reservation_size():
        # get user main menu input
        main_menu_choice = input()
        # if user chooses reservation, ask for party size
        if main_menu_choice.lower() == 'r' or main_menu_choice.lower() == 'reservation':
            size = int(input('Please enter the size of your party: '))
            return size
        # any other choice, exit system
        else:
            print('Thank you for using MyTable! Have a wonderful day!')
            sys.exit()

    # display the main menu
    display_main_menu_options()

    total = total_seats()
    occupied = occupied_seats(total)
    available = available_seats(total, occupied)

    reservation_size()


main()
