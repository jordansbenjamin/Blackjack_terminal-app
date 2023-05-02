##### WINNER SECTION #####
from calculate import calculate_score
from player import player_hand
from dealer import dealer_hand

def determine_winner():
    '''This function involves the logic for determining conditions of winner and displaying the final score and outcome'''
    # Sum up final player and dealer score
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)
    # Display both players and dealers final hand and their final score
    print("\n")
    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Dealers final hand: {dealer_hand}, final score: {dealer_score}")
    print("\n")
    # Determine condition of winner/loser based on Natural Blackjack, which means that they have a 21 from the first cards dealt, return their outcome
    if player_score == 21 and len(player_hand) == 2:
        return "Instant win! With a natural Blackjack 🤠"
    elif dealer_score == 21 and len(dealer_hand) == 2:
        return "You lose! Dealer wins with a natural Blacjack 🤯"
    # Determine condition of winner/loser based on normal Blackjack, which means that they have a 21 from cards drawn throughout the game, return their outcome
    if player_score == 21:
        return "You won with a Blackjack! 😎"
    elif dealer_score == 21:
        return "You lose! Dealer wins with a Blackjack 😤"
    # Determine all other possible winning/losing conditions, return their outcome
    if player_score > 21:
        return "You went over! And that's game over.. 😩"
    elif dealer_score > 21:
        return "Dealer went over.. Lucky you, you win! 😅"
    elif player_score > dealer_score:
        return "You're a winner! You have a higher score than the Dealer 🥳"
    elif player_score < dealer_score:
        return "You lost... The dealer has a higher score 🙃"
    elif player_score == dealer_score:
        return "It's a draw! 🥲"