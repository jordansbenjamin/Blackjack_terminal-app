##### MAIN SECTION #####
import csv
from clear import clear_screen
from art import main_logo, thanks_logo
from calculate import calculate_score
from player import player_turn, player_hand
from dealer import dealer_turn, dealer_hand
from cards import init_deck
from winner import determine_winner
from menu import menu, instructions, rules, history
from history import create_csv_file, view_game_history, write_game_history
from abstractions import init_deal, print_first_hand_and_score

def play_blackjack():
    '''This functions serves as the main function body of the program that includes other parts, section and functions of the program. All combined together to serves as the main flow which runs to play the Blackjack program'''

    print(main_logo)
    init_deal()
    # Prints first hand of player and dealer along with their score
    print_first_hand_and_score()

    # Start of players turn
    player_turn()
    # Start of dealers turn
    dealer_turn()
    # Determines winner and displays outcome of the game
    winner = determine_winner()
    # print(winner)
    # Calculates score for final hand, cannot be abstracted as variable needs to be accessed as it is used as arguments
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)
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
    clear_screen()
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