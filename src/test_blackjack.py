##### TESTING #####
from pytest import *
from main import *
from player import *
from dealer import *
from calculate import *
from winner import *

# NOTE: Running tests works with the command(pytest -s)

### TEST 1 ###
# CALCULATE SCORE FUNCTION 
"""This test will assert if the function for calculating the score from the list of cards adds up correctly and returns the correct sum"""
def test_calculate_score():
    # TEST CASE 1: Test player with a hand of two cards and test the return of the sum
    player_hand = ['♦2', '♠8']
    # Expected score
    expected_player_score = 10
    # Expected Result: Pass
    assert calculate_score(player_hand) == expected_player_score
    # Result: Pass ✅

    # TEST CASE 2: Test dealer with a hand of four cards and test the return of the sum
    dealer_hand = ['♣5', '♥7', '♠3', '♦4',]
    # Expected score
    expected_dealer_score = 19
    # Expected Result: Pass
    assert calculate_score(dealer_hand) == expected_dealer_score
    # Result: Pass ✅

    # TEST CASE 3: Test player with a hand of six cards and test the return of the sum
    player_hand = ['♣4', '♥2', '♦4', '♠8', '♦2', '♠8']
    # Expected score
    expected_player_score = 28
    # Expected Result: Pass
    assert calculate_score(player_hand) == expected_player_score
    # Result: Pass ✅

    # TEST CASE 4: Test dealer with natural Blacjack hand (two cards) and returns the sum
    dealer_hand = ['♥A', '♦K']
    # Expected score
    expected_dealer_score = 21
    # Expected Result: Pass
    assert calculate_score(dealer_hand) == expected_dealer_score
    # Result: Pass ✅

### TEST 2 ###
# DETERMINE WINNER FUNCTION
"""This test will assert the correct expected outcome of various winning conditions of the game for both the player and dealer based on the score they have and returns the outcome (win/lose)"""
def test_determine_winner():
    # TEST CASE 1: Test the condition when the player recieves a natural Blackjack and returns the correct output
    # Player hand with a natural Blackjack (score of 21)
    # Dealer hand score sums to 10
    # Expected outcome: Player wins the game from a natural Blackjack
    if player_hand == ['♥A', '♦K'] and dealer_hand == ['♦2', '♠8']:
        expected_output = "Instant win! With a natural Blackjack 🤠"
        # Expected Result: Pass
        assert determine_winner(player_hand, dealer_hand) == expected_output

    # TEST CASE 2: Test the condition when the dealer recieves a natural Blackjack and returns the correct output
    # Dealer hand with a natural Blackjack (score of 21)
    # Player hand score sums to 11
    # Expected outcome: Dealer wins the game from a natural Blackjack and Player loses
    elif dealer_hand == ['♥A', '♦Q'] and player_hand == ['♦4', '♠7']:
        expected_output = "You lose! Dealer wins with a natural Blacjack 🤯"
        # Expected Result: Pass
        assert determine_winner(player_hand, dealer_hand) == expected_output

    # TEST CASE 3: Test the condition when the player recieves a normal Blackjack and returns the correct output
    # Player hand with a normal Blackjack (total score of 21)
    # Dealer hand score sums to 7
    # Expected outcome: Player wins the game from a normal Blackjack
    elif player_hand == ['♥7', '♦10', '♠4'] and dealer_hand == ['♦2', '♠5']:
        expected_output = "You won with a Blackjack! 😎"
        # Expected Result: Pass
        assert determine_winner(player_hand, dealer_hand) == expected_output

    # TEST CASE 4: Test the condition when the dealer recieves a normal Blackjack and returns the correct output
    # Dealer hand with a natural Blackjack (score of 21)
    # Player hand score sums to 11
    # Expected outcome: Dealer wins the game from a natural Blackjack and Player loses
    elif dealer_hand == ['♥A', '♦Q'] and player_hand == ['♦4', '♠7']:
        expected_output = "You lose! Dealer wins with a Blackjack 😤"
        # Expected Result: Pass
        assert determine_winner(player_hand, dealer_hand) == expected_output

    # TEST CASE 5: Test the condition when the players hand goes over 21 and returns the correct output
    # Player hand sums to 22 which is over 21
    # Dealer hand score sums to 17
    # Expected outcome: Player loses the game with an overdrawn hand
    elif player_hand == ['♥7', '♦6', '♠4', '♣5'] and dealer_hand == ['♦2', '♠5', '♦J']:
        expected_output = "You went over! And that's game over.. 😩"
        # Expected Result: Pass
        assert determine_winner(player_hand, dealer_hand) == expected_output

    # TEST CASE 6: Test the condition when the dealer's hand goes over 21 and returns the correct output
    # Dealer hand sums up to 26 which is over 21
    # Player hand score sums to 13
    # Expected outcome: Dealer loses the game with an overdrawn hand, Player wins
    elif dealer_hand == ['♥7', '♦6', '♠3', '♣10'] and player_hand == ['♦4', '♠9']:
        expected_output = "Dealer went over.. Lucky you, you win! 😅"
        # Expected Result: Pass
        assert determine_winner(player_hand, dealer_hand) == expected_output

    # TEST CASE 7: Test the condition when the players hand is higher than the dealers hand and returns the correct output
    # Player hand score sums to 16
    # Dealer hand score sums to 13
    # Expected outcome: Player wins the game with a higher hand
    elif player_hand == ['♥7', '♦5', '♠4'] and dealer_hand == ['♦2', '♠5', '♦6']:
        expected_output = "You're a winner! You have a higher score than the Dealer 🥳"
        # Expected Result: Pass
        assert determine_winner() == expected_output

    # TEST CASE 8: Test the condition when the dealers hand is higher than the players hand and returns the correct output
    # Dealers hand sums up to 18
    # Player hand score sums to 15
    # Expected outcome: Dealer wins the game with a higher hand
    elif dealer_hand == ['♥8', '♠3', '♣10'] and player_hand == ['♦4', '♠9', '♥2' ]:
        expected_output = "You lost... The dealer has a higher score 🙃"
        # Expected Result: Pass
        assert determine_winner() == expected_output

    # TEST CASE 8: Final condition where both the players and dealers hand total score equals each other and returns the correct output
    # Dealer hand sums up to 19
    # Player hand score sums to 19
    # Expected outcome: Both the player and dealer draws
    elif dealer_hand == ['♥3', '♦6', '♣10'] and player_hand == ['♦4', '♠9', '♥6']:
        expected_output = "It's a draw! 🥲"
        # Expected Result: Pass
        assert determine_winner() == expected_output