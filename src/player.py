##### PLAYER SECTION #####
from calculate import calculate_score
from cards import deal_card

# TODO 1: Create empty player cards list
player_cards = []
# TODO 2: Create players function which involves logic of players turns
def player_():
    # TODO 3: Calculate score
    player_score = calculate_score(player_cards)
    # TODO 4: Display hand and current score
    print(f"Your current hand: {player_cards}, current score: {player_score}")

    # TODO 5: Check if score is 21, if so players turn automatically ends
    if player_score == 21:
        return
    # TODO 6: Create while loop to prompt player if they want to draw a card, if players score is 21 or over, players turn ends
    while input("Do you want to 'hit' for another card or 'pass' your turn? ") == 'hit':
        print("\n")
        deal_card(1, player_cards)
        player_score = calculate_score(player_cards)
        if player_score == 21:
            return
        elif player_score > 21:
            return

deal_card(2, player_cards)
player_()


