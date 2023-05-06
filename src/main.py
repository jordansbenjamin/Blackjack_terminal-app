##### MAIN SECTION #####
from colored import fg, attr
from clear import clear
from art import main_logo, thanks_logo
from calculate import calculate_score
from player import player_turn, player_hand
from dealer import dealer_turn, dealer_hand
from cards import init_deck
from winner import determine_winner
from menu import menu, instructions, rules, history, wipe_history
from history import create_csv_file, write_game_history
from abstractions import *

def play_blackjack():
    '''This functions serves as the main function body of the program that includes other parts, section and functions of the program. All combined together to serves as the main flow which runs to play the Blackjack program'''
    
    try:
        # Starts the game on a clean slate, clearing the player and dealers hand and clears screen
        clean_slate()
        print(main_logo)
        # Initially deals 2 cards for player to start the game and 1 card for dealer
        init_deal()
        # Prints first hand of player and dealer along with their score
        print_first_hand_and_score()
        # Start of players turn
        player_turn()
        # Start of dealers turn
        dealer_turn()
        # Determines winner and displays outcome of the game
        winner = determine_winner()
        # Calculates score for final hand, cannot be abstracted as variable needs to be accessed as it is used as arguments
        player_score, dealer_score = calculate_score(player_hand), calculate_score(dealer_hand)
        # Writes game results to CSV
        write_game_history(player_hand, player_score, dealer_hand, dealer_score, winner)

        while True:
            try:
                play = input(f"Continue playing a game of Blackjack? Type {fg(2)}{attr('bold')}'y'{attr('reset')} to continue or {fg(196)}{attr('bold')}'b'{attr('reset')} to go back to main menu: ").lower().strip(' ')
                
                match play:
                    case 'y':
                        # Recursively starts the game for another round
                        play_blackjack()
                        break
                    case 'b':
                        # Exits loop and function to go back to main menu
                        clear()
                        break
                    case _:
                        clear()
                        raise ValueError(f"{fg(9)}{attr(1)}\nInvalid Input! Please enter 'y' or 'b':{attr('reset')}\n")
            except ValueError as InvalidInput:
                print(InvalidInput)
                enter_to_continue()
                clear()
    except KeyboardInterrupt:
        exit_game_to_menu()

def main_menu():
    '''This function serves as the main menu which introduces the user to the program and so the user can interact and navigate throughout the program'''

    try:
        clear()
        user_choice = ''

        while user_choice != '6':

            print(main_logo)
            print(f"{attr(1)}Welcome to {fg(196)}Blackjack ♠️{attr('reset')}  {attr(1)}Please choose from the following options:{attr('reset')}\n")
            user_choice = menu()

            try:
                match user_choice:
                    case '1':
                        # Recursively starts the game or to go for another round after navigating menu
                        # clean_slate()
                        play_blackjack()
                    case '2':
                        # This will get you to view the instructions for the game, leaving the menu
                        instructions()
                    case '3':
                        # This will get you to view the house rules of the game, leaving the menu
                        rules()
                    case '4':
                        # This will get you to view the history and score for the game, leaving the menu
                        history()
                    case '5':
                        # This will let the user decide if they want to wipe out the game history
                        wipe_history()
                    case '6':
                        # Exits the program entirely
                        clear()
                        print(thanks_logo)
                        break
                    case _:
                        clear()
                        raise ValueError(f"{fg(196)}{attr(1)}Invalid Input! Please enter a numbered option from the menu (1-6):{attr('reset')}\n")
            except ValueError as InvalidInput:
                print("\n" + str(InvalidInput))
                enter_to_continue()
                clear()
    except KeyboardInterrupt:
        exit_game()

if __name__ == '__main__':
    create_csv_file()
    init_deck()
    main_menu()