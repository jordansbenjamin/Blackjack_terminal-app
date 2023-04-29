##### MAIN SECTION #####
from clear import clear_screen
from art import logo
from calculate import calculate_score
from player import player_turn, player_hand
from dealer import dealer_turn, dealer_hand
from cards import init_deck, deal_card

# TODO 1: Create a function that will serve as the main function body of the program that will include other parts, sections and functions of the program, this main function will serve as the main flow running the program
def play_blackjack():
    # TODO LATE: Add game logo here
    print(logo)

    # Both player and dealer initially gets dealt 2 cards
    deal_card(2, player_hand)
    deal_card(2, dealer_hand)

    player_score = calculate_score(player_hand)
    print(f"Your first hand: {player_hand}, current score: {player_score}")
    dealer_score = calculate_score(dealer_hand)
    print(f"Dealers first card: {dealer_hand[0]}, current score: {dealer_score}")

    # Start of players turn
    player_turn()
    # Start of dealers turn
    dealer_turn()

# TODO 2: Initialise the deck
init_deck()

# TODO 3: Create a while loop that will prompt the user if they want to continue playing, if yes then call the main function to start the game
while True:
    play = input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ").lower()
    
    if play == 'yes':
        # TODO LATER: Add clear function here
        player_hand.clear()
        dealer_hand.clear()
        clear_screen()
        play_blackjack()
    elif play == 'no':
        break
    else:
        print("Invalid input, please enter 'yes' or 'no'.")
