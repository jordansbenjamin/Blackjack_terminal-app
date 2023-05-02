##### MAIN SECTION #####
import csv
from clear import clear_screen
from art import main_logo, thanks_logo
from calculate import calculate_score
from player import player_turn, player_hand
from dealer import dealer_turn, dealer_hand
from cards import init_deck, deal_card
from winner import determine_winner
from menu import menu, instructions, rules, history
from history import create_csv_file, view_game_history, write_game_history

def play_blackjack():
    '''This functions serves as the main function body of the program that includes other parts, section and functions of the program. All combined together to serves as the main flow which runs to play the Blackjack program'''

    print(main_logo)

    # Player initially gets dealt 2 cards, dealer gets dealt 1 only because first card is revealed
    deal_card(2, player_hand)
    deal_card(1, dealer_hand)

    # Players score is added and their first hand is revealed
    player_score = calculate_score(player_hand)
    print(f"Your first hand: {player_hand}, current score: {player_score}")
    # Dealers score is added, however only their first card is revealed
    dealer_score = calculate_score(dealer_hand)
    print(f"Dealers first card: {dealer_hand}, current score: {dealer_score}")

    # Start of players turn
    player_turn()
    # Start of dealers turn
    dealer_turn()
    # Determines winner and displays outcome of the game
    winner = determine_winner()
    print(winner)

    # TODO 1: Write game results to CSV and create a variable that stores the count games function
    write_game_history(player_hand, player_score, dealer_hand, dealer_score, winner)

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
# init_deck()

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
                # print("You are viewing the score history.")
                # TODO 2: Add view history function here
                # view_game_history()
                history()
            case '5':
                clear_screen()
                print(thanks_logo)
                break
            case _:
                print("Invalid input")

# The main menu appears first to introduce the user to the program
# main_menu()

if __name__ == '__main__':
    create_csv_file()
    init_deck()
    main_menu()