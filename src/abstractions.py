##### ABSTRACTIONS #####
from colored import fg, attr
from clear import clear
from cards import deal_card
from player import player_hand
from dealer import dealer_hand
from calculate import calculate_score
from art import thanks_logo

def init_deal():
    '''This function initially deals 2 cards for the player, dealer gets dealt 1 card only because first card is revealed'''

    deal_card(2, player_hand)
    deal_card(1, dealer_hand)

def print_first_hand_and_score():
    '''This function prints the first hand of the player and dealer, it also prints their current score'''

    # Players score is added and their first hand is revealed
    player_score = calculate_score(player_hand)
    print(f"{attr(1)}{fg(21)}Your first hand:{attr('reset')} {player_hand}, {attr(1)}{fg(21)}current score:{attr('reset')} {player_score}")
    # Dealers score is added, however only their first card is revealed
    dealer_score = calculate_score(dealer_hand)
    print(f"{attr(1)}{fg(21)}Dealers first card:{attr('reset')} {dealer_hand}, {attr(1)}{fg(21)}current score:{attr('reset')} {dealer_score}")

def clean_slate():
    '''This function resets the players and dealers hand for a clean slate before starting another game, additionally clears the screen'''
    
    player_hand.clear()
    dealer_hand.clear()
    clear()

def exit_game_to_menu():
    '''This function handles the exception message for the user when exiting the game using the ctrl + c command and leads them back to the main menu'''

    clear()
    print(f"{fg(9)}{attr(1)}\nYou have stopped playing Blackjack. You will now be returned to the main menu.{attr('reset')}\n")
    input(f"{fg(2)}{attr(1)}Press Enter to continue...{attr('reset')}")
    clear()

def exit_game():
    '''This function handles the exception message for the user when exiting the game using the ctrl + c command and exits the program entirely'''

    clear()
    print(f"{fg(9)}{attr(1)}\nYou have stopped playing Blackjack. You will now exit the game.{attr('reset')}\n")
    input(f"{fg(2)}{attr(1)}Press Enter to exit...{attr('reset')}")
    clear()
    print(thanks_logo)

def enter_to_continue():
    '''This function simply abstracts the enter continue input'''
    input(f"{fg(2)}{attr(1)}Press Enter to continue...{attr('reset')}")