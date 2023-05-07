##### WINNER SECTION #####
from colored import fg, attr
from calculate import calculate_score
from player import player_hand
from dealer import dealer_hand
from cards import deal_card

def determine_winner():
    '''This function involves the logic for determining conditions of winner and displaying the final score and outcome'''
    
    # Sum up final player and dealer score
    player_score, dealer_score = calculate_score(player_hand), calculate_score(dealer_hand)
    # Display both players and dealers final hand and their final score
    print(f"\n{attr(1)}{fg(21)}Your final hand:{attr('reset')} {player_hand}, {attr(1)}{fg(21)}final score:{attr('reset')} {player_score}")
    print(f"{attr(1)}{fg(21)}Dealers final hand:{attr('reset')} {dealer_hand}, {attr(1)}{fg(21)}final score:{attr('reset')} {dealer_score}\n")
    # Determine condition of winner/loser based on Natural Blackjack, which means that they have a 21 from the first cards dealt, return their outcome
    if player_score == 21 and len(player_hand) == 2:
        result = "Instant win! With a natural Blackjack 🤠\n"
    elif dealer_score == 21 and len(dealer_hand) == 2:
        result = "You lose.. Dealer wins with a natural Blacjack 🤯\n"
    # Determine condition of winner/loser based on normal Blackjack, which means that they have a 21 from cards drawn throughout the game, return their outcome
    elif player_score == 21:
        result = "You won with a Blackjack! 😎\n"
    elif dealer_score == 21:
        result = "You lose.. Dealer wins with a Blackjack 😤\n"
    # Determine all other possible winning/losing conditions, return their outcome
    elif player_score > 21:
        result = "Bust! You lost.. 😩\n"
    elif dealer_score > 21:
        result = "Dealer bust! Lucky you, you win! 😅\n"
    elif player_score > dealer_score:
        result = "You're a winner! You have a higher score than the Dealer 🥳\n"
    elif player_score < dealer_score:
        result = "You lost... The dealer has a higher score 🙃\n"
    else:
        result = "It's a draw! 🥲\n"
    
    print(result)
    return result