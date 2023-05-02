##### DEALER SECTION #####
from calculate import calculate_score
from cards import draw_card
from player import player_hand

# Initialise empty dealer hand list, requires this to be global as it is accessed various times throughout the program
dealer_hand = []

def dealer_turn():
    '''This function involves logic of dealers turns and play'''
    
    # The codes below to calculate score is required as it is used for conditional statements to check
    dealer_score = calculate_score(dealer_hand)
    player_score = calculate_score(player_hand)
    # Dealer doesn't have to draw another card if certain conditions are met: Player bust, dealer score higher, or dealer has BJ
    if player_score > 21 or dealer_score > player_score or dealer_score == 21:
        return
    # If dealers hand score is under 17, keep drawing cards
    while dealer_score < 17:
        card = draw_card()
        dealer_hand.append(card)
        # This code is required as the conditions checks the update hand/score
        dealer_score = calculate_score(dealer_hand)
        # Conditions for dealer
        if dealer_score == 21: # If dealer BJ, turn ends
            return
        elif dealer_score > 21: # If dealer bust, turn ends
            return
    return