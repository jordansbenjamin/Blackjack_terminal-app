##### MAIN SECTION #####
from clear import clear_screen
from art import main_logo
from calculate import calculate_score
from player import player_turn, player_hand
from dealer import dealer_turn, dealer_hand
from cards import init_deck, deal_card
from winner import determine_winner
from menu import menu, instructions, rules

def play_blackjack():
    '''This functions serves as the main function body of the program that includes other parts, section and functions of the program. All combined together to serves as the main flow which runs to play the Blackjack program'''

    print(main_logo)

    # Both player and dealer initially gets dealt 2 cards
    deal_card(2, player_hand)
    deal_card(1, dealer_hand)

    # Players score is added and their first hand is revealed
    player_score = calculate_score(player_hand)
    print(f"Your first hand: {player_hand}, current score: {player_score}")
    # Dealers score is added, however only their first card is revealed
    dealer_score = calculate_score(dealer_hand)
    print(f"Dealers first card: {dealer_hand}, current score: {dealer_score}")
    # NOTE: THE ABOVE CODE IS DRY?

    # Start of players turn
    player_turn()
    # Start of dealers turn
    dealer_turn()
    # Determines winner and displays outcome of the game
    winner = determine_winner()
    print(winner)
    while True:
        play = input("Do you want to continue playing a game of Blackjack? Type 'yes' to continue or 'no' to go back to main menu: ").lower()
        
        match play:
            case 'yes':
                player_hand.clear()
                dealer_hand.clear()
                clear_screen()
                play_blackjack()
                break
            case 'no':
                clear_screen()
                break
            case _:
                print("Invalid input, please enter 'yes' or 'no'.")

# Initialises the deck of cards at the start of every game for a fresh start
init_deck()

def main_menu():
    '''This function serves as the main menu which introduces the user to the program and so the user can interact and navigate throughout the program'''
    user_choice = ''
    while user_choice != '5':
        print(main_logo)
        print("Welcome to Blackjack ♠️ Please choose from the following options:")
        
        user_choice = menu()

        match user_choice:
            case '1':
                player_hand.clear()
                dealer_hand.clear()
                clear_screen()
                play_blackjack()
            case '2':
                instructions()
            case '3':
                rules()
            case '4':
                print("You are viewing the score history.")
            case '5':
                break
            case _:
                print("Invalid input")

# The main menu appears first to introduce the user to the program
main_menu()