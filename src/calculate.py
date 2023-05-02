#### CALCULATE SCORES ####
from cards import cards_dict

def calculate_score(player_or_dealer_hand):
    '''This function calculates the scores of the cards from a hand, the parameter will be the hand itself, start a score from 0'''
    
    score = 0
    cards = []
    # Remove suits and put it into a cards list for calculation
    for card in player_or_dealer_hand:
        cards.append(card[1:])
    # Converts any picture cards to a score of 10 and Ace to 11 using the cards dictionary
    for card in cards:
        score += cards_dict[card]
    # If Ace card/s are found and score is over 21, count Ace as 1 instead of 11
    aces = cards.count('A')
    for i in range(aces):
        if score > 21 and i == 1:
            score -= 10
        elif score > 21 and i > 1:
            score -= 1
        else:
            break
    return score