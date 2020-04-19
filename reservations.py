# reservations app

# add wait list functionality/queue

# import random module
import random

main_menu_options = [
    'Hello, welcome to (R)eserver! Please choose from the following options: ',
    'Make a reservation',
    'Exit'
]


def display_main_menu_options():
    print(main_menu_options[0])
    print(main_menu_options[1])
    print(main_menu_options[2])


def calculate_seats(party):
    # randomize the total amount of seats in the restaurant
    total_seats = random.randint(10, 25)
    print(f'number of seats in r: {total_seats}')

    # total occupied seats
    occupied_seats = random.randint(0, total_seats)
    print(f'occupied seats: {occupied_seats}')

    # available seats
    available_seats = total_seats - occupied_seats
    print(f'available seats: {available_seats}')

    if party <= available_seats and available_seats > 0:
        print(f'Thank you for your reservation for a party of {party}.')
        main_menu = False
    else:
        print(
            f'We are not able to create a reservation for your party of {party}. There are only{available_seats} available seats. Would you like to be put on the waitlist?')


# display the main menu
display_main_menu_options()

# initialize main menu
main_menu = True

# set main menu
while main_menu == True:
    # get user main menu input
    main_menu_choice = input()
    # if user makes reservation
    if main_menu_choice.lower() == 'r' or main_menu_choice.lower() == 'reservation' or main_menu_choice.lower() == 'make a reservation':
        # ask for party size
        party_size = int(input('What is the size of your party?: '))
        calculate_seats(party_size)
    elif main_menu_choice.lower() == 'exit':
        main_menu = False
        print('Thank you for visting (R)eserver! Have a wonderful day!')
    else:
        print('That is not a valid command. Please try again.')
        display_main_menu_options()
