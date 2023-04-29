##### MAIN SECTION #####
from player import player_
from dealer import dealer_
from cards import init_deck

# TODO 1: Create a function that will serve as the main function body of the program that will include other parts, sections and functions of the program, this main function will serve as the main flow running the program
def play_blackjack():
    # TODO LATE: Add game logo here

    player_()
    dealer_()

# TODO 2: Initialise the deck
init_deck()

# TODO 3: Create a while loop that will prompt the user if they want to continue playing, if yes then call the main function to start the game
while True:
    play = input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ").lower()
    
    if play == 'yes':
        # TODO LATER: Add clear function here
        play_blackjack()
    elif play == 'no':
        break
    else:
        print("Invalid input, please enter 'yes' or 'no'.")
