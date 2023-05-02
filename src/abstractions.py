##### ABSTRACTIONS #####
from cards import deal_card
from player import player_hand
from dealer import dealer_hand
from calculate import calculate_score
from clear import clear_screen

def init_deal():
    '''This function initially deals 2 cards for the player, dealer gets dealt 1 card only because first card is revealed'''

    deal_card(2, player_hand)
    deal_card(1, dealer_hand)

def print_first_hand_and_score():
    '''This function prints the first hand of the player and dealer, it also prints their current score'''

    # Players score is added and their first hand is revealed
    player_score = calculate_score(player_hand)
    print(f"Your first hand: {player_hand}, current score: {player_score}")
    # Dealers score is added, however only their first card is revealed
    dealer_score = calculate_score(dealer_hand)
    print(f"Dealers first card: {dealer_hand}, current score: {dealer_score}")

def clean_slate():
    '''This function resets the players and dealers hand for a clean slate before starting another game'''
    
    player_hand.clear()
    dealer_hand.clear()
    clear_screen()