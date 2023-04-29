##### DEALER SECTION #####
from calculate import calculate_score
from cards import draw_card

# TODO 1: Create empty dealer cards list
dealer_cards = []
# TODO 2: Create dealers function which involves logic of dealers turns and play
def dealer_():
    dealer_score = calculate_score(dealer_cards)
    player_score = calculate_score(player_cards)
    # TODO 3: Dealer doesn't have to draw another card if certain conditions are met: Player bust, dealer score higher, or dealer has BJ
    if player_score > 21 or dealer_score > player_score or dealer_score == 21:
        return
    # TODO 4: If dealers hand score is under 17, keep drawing cards (use while loop)
    while dealer_score < 17:
        card = draw_card()
        dealer_cards.append(card)
        dealer_score = calculate_score(dealer_cards)

        # Conditions for dealer
        if dealer_score == 21: # If dealer BJ, turn ends
            return
        elif dealer_score > 21: # If dealer bust, turn ends
            return
    return