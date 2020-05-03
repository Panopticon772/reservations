# reservations app

# add wait list functionality/queue

# import random module
import random

# import system module
import sys


def main():

    main_menu_options = [
        'Hello, welcome to MyTable!',
        '1) Make a reservation',
        '2) Exit'
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

    def make_reservation(choice):
        # if user chooses reservation, ask for party size
        if choice.lower() == '1' or choice.lower() == 'r' or choice() == 'reservation':
            size = int(input('Please enter the size of your party: '))
            return size
        # any other choice, exit system
        else:
            print('Thank you for using MyTable! Have a wonderful day!')
            sys.exit()

    def calculate_seats(size, available):
        # if size of party is less than available seats and available seats > 0, party is reserved, else ask for waitlist
        if size < available and available > 0:
            print(
                'Your seats have been reserved. Thank you for reserving with MyTable! Have a wonderful day!')
            sys.exit()
        else:
            print(
                f"We're sorry, but due to your party size of: {size}, your reservations were not able to be made. Would you like to be put on the waitlist?")
            return

    # display the main menu
    display_main_menu_options()

    # get the users input
    choice = input('Please select an option: ')

    # users decision
    size = make_reservation(choice)

    # total seats
    total = total_seats()

    # occupied
    occupied = occupied_seats(total)

    # available
    available = available_seats(total, occupied)

    # calculate
    calculate_seats(size, available)

    # waitlist

    # status check


main()
