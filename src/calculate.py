#### CALCULATE SCORES ####
from cards import cards_dict

# TODO 1: Create a function that calculates the scores of the cards from a hand, the parameter will be the hand itself, start a score from 0
def calculate_score(player_or_dealer_hand):
    score = 0
    # TODO 2: Remove suits and put it into a cards list for calculation
    cards = []
    for card in player_or_dealer_hand:
        cards.append(card[1:])
    # TODO 3: Convert any picture cards to a score of 10 and Ace to 11 using the cards dictionary
    for card in cards:
        score += cards_dict[card]
    # TODO 4: If Ace card/s are found and score is over 21, count Ace as 1 instead of 11
    aces = cards.count('A')
    for i in range(aces):
        if score > 21:
            score -= 10
        else:
            break
    return score

# TODO 2: Add function that caculates score into variable via parameter
# def add_score(score, hand):
#     score = calculate_score(hand)
#     print(f"Your current hand: {hand}, current score: {score}")